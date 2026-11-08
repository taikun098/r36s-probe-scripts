from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os

def load(p): return FdtBlobParse(open(p,'rb')).to_fdt()
def walk(n):
    yield n
    for s in n.subdata:
        if isinstance(s,FdtNode): yield from walk(s)
def prop_words(node,name):
    for it in node.subdata:
        if isinstance(it,FdtProperty) and it.get_name()==name and hasattr(it,'words'):
            return it.words
    return None

out=[]
def pr(s): out.append(s)

for panel in ['k36s','k36','r36t','r36xx']:
    try:
        pdir=os.path.join(r"E:\consoles",panel)
        dtb=os.path.join(pdir,[x for x in os.listdir(pdir) if x.endswith('.dtb')][0])
        f=load(dtb); root=f.get_rootnode()
        phmap={}
        for n in walk(root):
            for it in n.subdata:
                if isinstance(it,FdtProperty) and it.get_name()=='phandle':
                    try: phmap[it.words[0]]=n.get_name()
                    except: pass
        pr(f"===== {panel} ({os.path.basename(dtb)}, {os.path.getsize(dtb)}B) =====")
        found=False
        for n in walk(root):
            if isinstance(n,FdtNode) and any(k in n.get_name().lower() for k in ('panel','dsi','lcd','display','mipi')):
                found=True
                compat=[it.strings for it in n.subdata if isinstance(it,FdtProperty) and it.get_name()=='compatible']
                init=None
                for it in n.subdata:
                    if isinstance(it,FdtProperty) and it.get_name()=='panel-init-sequence' and hasattr(it,'bytes'):
                        init=len(it.bytes)
                def fmt(g):
                    if not g or len(g)<3: return str(g)
                    return "%s pin%d flags%d"%(phmap.get(g[0],'ph%d'%g[0]),g[1],g[2])
                pr(f"  {n.get_name()}: compat={compat} init={init}B reset={fmt(prop_words(n,'reset-gpios'))} enable={fmt(prop_words(n,'enable-gpios'))} power={prop_words(n,'power-supply')}")
        if not found:
            pr("  (no panel/dsi/lcd node found)")
    except Exception as e:
        pr(f"[{panel}] ERR {repr(e)}")

open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\k36_result.txt",'w',encoding='utf-8').write("\n".join(out))
print("done")
