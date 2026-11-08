from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os

def load(p): return FdtBlobParse(open(p,'rb')).to_fdt()
def walk(n):
    yield n
    for s in n.subdata:
        if isinstance(s,FdtNode): yield from walk(s)

panel='k36s'
pdir = os.path.join(r"E:\consoles", panel)
dtb = os.path.join(pdir, [x for x in os.listdir(pdir) if x.endswith('.dtb')][0])
print("dtb:", dtb, "size:", os.path.getsize(dtb))
f = load(dtb)
root=f.get_rootnode()
phmap={}
for n in walk(root):
    for it in n.subdata:
        if isinstance(it,FdtProperty) and it.get_name()=='phandle':
            try: phmap[it.words[0]]=n.get_name()
            except: pass

# find any node mentioning panel or dsi or lcd or mipi
for n in walk(root):
    name=n.get_name().lower()
    if any(k in name for k in ('panel','dsi','lcd','mipi','display')):
        print("NODE:", n.get_name(), "path-check...")
# print child nodes of root to see structure
def props(n):
    out=[]
    for it in n.subdata:
        if isinstance(it,FdtProperty):
            out.append(it.get_name())
    return out
print("=== root children ===")
for s in root.subdata:
    if isinstance(s,FdtNode):
        print("  ", s.get_name(), props(s))
