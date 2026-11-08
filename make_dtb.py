import copy
from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty, FdtPropertyStrings, FdtPropertyWords, FdtPropertyBytes

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(p):
    return FdtBlobParse(open(p, 'rb')).to_fdt()

def walk(node, fn):
    fn(node)
    for s in node.subdata:
        if isinstance(s, FdtNode):
            walk(s, fn)

def find_prop(node, name):
    for it in node.subdata:
        if isinstance(it, FdtProperty) and it.get_name() == name:
            return it
    return None

ark = load(base + r"\origin_p1.dtb")
orig = load(base + r"\evb_orig.dtb")

# collect all phandles in ark tree
ark_phandles = set()
def collect_ph(n):
    for it in n.subdata:
        if isinstance(it, FdtProperty) and it.get_name() == 'phandle':
            try: ark_phandles.add(it.words[0])
            except Exception: pass
walk(ark.get_rootnode(), collect_ph)

ark_p = ark.resolve_path('/dsi@ff450000/panel@0')
orig_p = orig.resolve_path('/dsi@ff450000/panel@0')

# orig values
orig_compat = find_prop(orig_p, 'compatible').strings
orig_init_raw = find_prop(orig_p, 'panel-init-sequence').bytes
orig_init = list(orig_init_raw)  # pyfdt bytes are already signed
orig_exit = find_prop(orig_p, 'panel-exit-sequence').words
orig_dt = None
for s in orig_p.subdata:
    if isinstance(s, FdtNode) and s.get_name() == 'display-timings':
        orig_dt = s; break

# deepcopy dt subtree, renumber phandles to avoid clash with ark
new_dt = copy.deepcopy(orig_dt)

# find all phandle props inside new_dt (incl. dt node and timing subnodes)
dt_nodes = [new_dt] + [s for s in new_dt.subdata if isinstance(s, FdtNode)]
ph_props = []
for n in dt_nodes:
    it = find_prop(n, 'phandle')
    if it: ph_props.append(it)
native = find_prop(new_dt, 'native-mode')

used = set(ark_phandles)
next_ph = 1000
mapping = {}
for it in ph_props:
    old = it.words[0]
    while next_ph in used:
        next_ph += 1
    mapping[old] = next_ph
    it.words[0] = next_ph
    used.add(next_ph)
    next_ph += 1
# update native-mode reference if it pointed to a remapped phandle
if native and native.words[0] in mapping:
    native.words[0] = mapping[native.words[0]]

# rebuild ark_p.subdata with replacements
new_sub = []
replaced = {'compatible':False,'init':False,'exit':False,'dt':False}
for item in ark_p.subdata:
    if isinstance(item, FdtProperty):
        n = item.get_name()
        if n == 'compatible':
            new_sub.append(FdtPropertyStrings('compatible', orig_compat)); replaced['compatible']=True; continue
        if n == 'panel-init-sequence':
            new_sub.append(FdtPropertyBytes('panel-init-sequence', orig_init)); replaced['init']=True; continue
        if n == 'panel-exit-sequence':
            new_sub.append(FdtPropertyWords('panel-exit-sequence', orig_exit)); replaced['exit']=True; continue
    if isinstance(item, FdtNode) and item.get_name() == 'display-timings':
        new_sub.append(new_dt); replaced['dt']=True; continue
    new_sub.append(item)
ark_p.subdata = new_sub

data = ark.to_dtb()
out = base + r"\r36s_st7703.dtb"
with open(out, 'wb') as fh:
    fh.write(data)
print("written", out, len(data), "bytes")
print("replaced:", replaced)
print("phandle map:", mapping)
