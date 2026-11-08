from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os, re

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"
out = base + r"\r36s_st7703.dtb"
print("exists:", os.path.exists(out), "size:", os.path.getsize(out) if os.path.exists(out) else 0)
b = open(out,'rb').read()
print("magic:", b[:4].hex())

def load(p):
    return FdtBlobParse(open(p,'rb')).to_fdt()
def find_prop(n,name):
    for it in n.subdata:
        if isinstance(it,FdtProperty) and it.get_name()==name: return it
    return None
def find_node(n,name):
    for it in n.subdata:
        if isinstance(it,FdtNode) and it.get_name()==name: return it
    return None

f = load(out)
p = f.resolve_path('/dsi@ff450000/panel@0')
print("compatible:", find_prop(p,'compatible').strings)
init = find_prop(p,'panel-init-sequence')
print("init-seq len:", len(init.bytes))
print("exit-seq:", find_prop(p,'panel-exit-sequence').words)
dt = find_node(p,'display-timings')
print("display-timings subnodes:", [s.get_name() for s in dt.subdata if isinstance(s,FdtNode)])
for sub in dt.subdata:
    if isinstance(sub,FdtNode):
        vals={pr.get_name(): (pr.words if hasattr(pr,'words') else None) for pr in sub.subdata if isinstance(pr,FdtProperty)}
        print("  ["+sub.get_name()+"]", vals)
nm = find_prop(dt,'native-mode')
print("native-mode:", nm.words if nm else None)
