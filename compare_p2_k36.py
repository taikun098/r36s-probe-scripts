from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os, hashlib

def load(p): return FdtBlobParse(open(p,'rb')).to_fdt()

def panel_node(f):
    return f.resolve_path('/dsi@ff450000/panel@0')

def dump_panel_props(f, label, out):
    p=panel_node(f)
    out.append(f"--- {label} panel@0 ---")
    for it in p.subdata:
        if isinstance(it,FdtProperty):
            n=it.get_name()
            if hasattr(it,'strings') and it.strings:
                out.append(f"  {n} = {it.strings}")
            elif hasattr(it,'words'):
                out.append(f"  {n} = {it.words}")
            elif hasattr(it,'bytes'):
                b=bytes((x & 0xFF) for x in it.bytes)
                out.append(f"  {n} = <{len(b)} bytes> sha={hashlib.sha256(b).hexdigest()[:16]}")
    # dsi node
    d=f.resolve_path('/dsi@ff450000')
    out.append(f"--- {label} dsi@ff450000 ---")
    for it in d.subdata:
        if isinstance(it,FdtProperty):
            n=it.get_name()
            if hasattr(it,'strings') and it.strings: out.append(f"  {n} = {it.strings}")
            elif hasattr(it,'words'): out.append(f"  {n} = {it.words}")

out=[]
pdir=lambda p: os.path.join(r"E:\consoles",p)
for p in ['clone type1 panel2','k36s','r36t']:
    dtb=os.path.join(pdir(p),[x for x in os.listdir(pdir(p)) if x.endswith('.dtb')][0])
    dump_panel_props(load(dtb), p, out)

open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\compare_p2_k36.txt",'w',encoding='utf-8').write("\n".join(out))
print("done")
