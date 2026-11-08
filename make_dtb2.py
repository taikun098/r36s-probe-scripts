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

# collect ark phandles
ark_ph = set()
def collect(n):
    for it in n.subdata:
        if isinstance(it, FdtProperty) and it.get_name() == 'phandle':
            try: ark_ph.add(it.words[0])
            except Exception: pass
walk(ark.get_rootnode(), collect)

ark_p = ark.resolve_path('/dsi@ff450000/panel@0')
orig_p = orig.resolve_path('/dsi@ff450000/panel@0')

# ST7703 values from orig (KEEP compatible as simple-panel-dsi = ArkOS original)
orig_init = list(find_prop(orig_p, 'panel-init-sequence').bytes)  # signed ok
orig_exit = find_prop(orig_p, 'panel-exit-sequence').words
orig_dsi_flags = find_prop(orig_p, 'dsi,flags').words
orig_dsi_format = find_prop(orig_p, 'dsi,format').words
orig_dsi_lanes = find_prop(orig_p, 'dsi,lanes').words
orig_dt = None
for s in orig_p.subdata:
    if isinstance(s, FdtNode) and s.get_name() == 'display-timings':
        orig_dt = s; break

# deepcopy dt, renumber phandles
new_dt = copy.deepcopy(orig_dt)
dt_nodes = [new_dt] + [s for s in new_dt.subdata if isinstance(s, FdtNode)]
ph_props = [find_prop(n, 'phandle') for n in dt_nodes]
ph_props = [p for p in ph_props if p]
native = find_prop(new_dt, 'native-mode')
used = set(ark_ph); next_ph = 1000; mapping = {}
for it in ph_props:
    old = it.words[0]
    while next_ph in used: next_ph += 1
    mapping[old] = next_ph
    it.words[0] = next_ph
    used.add(next_ph); next_ph += 1
if native and native.words[0] in mapping:
    native.words[0] = mapping[native.words[0]]

# rebuild ark_p.subdata: replace init/exit/dsi params/display-timings, KEEP compatible
new_sub = []
replaced = {'init':False,'exit':False,'dsi':False,'dt':False}
for item in ark_p.subdata:
    if isinstance(item, FdtProperty):
        n = item.get_name()
        if n == 'panel-init-sequence':
            new_sub.append(FdtPropertyBytes('panel-init-sequence', orig_init)); replaced['init']=True; continue
        if n == 'panel-exit-sequence':
            new_sub.append(FdtPropertyWords('panel-exit-sequence', orig_exit)); replaced['exit']=True; continue
        if n in ('dsi,flags','dsi,format','dsi,lanes'):
            vals = {'dsi,flags':orig_dsi_flags,'dsi,format':orig_dsi_format,'dsi,lanes':orig_dsi_lanes}[n]
            new_sub.append(FdtPropertyWords(n, vals)); replaced['dsi']=True; continue
    if isinstance(item, FdtNode) and item.get_name() == 'display-timings':
        new_sub.append(new_dt); replaced['dt']=True; continue
    new_sub.append(item)
ark_p.subdata = new_sub

data = ark.to_dtb()
out = base + r"\r36s_simplepanel_st7703.dtb"
with open(out, 'wb') as fh:
    fh.write(data)
print("written", out, len(data), "bytes")
print("replaced:", replaced)
