from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os

def load(p): return FdtBlobParse(open(p,'rb')).to_fdt()
def prop_words(node,name):
    for it in node.subdata:
        if isinstance(it,FdtProperty) and it.get_name()==name and hasattr(it,'words'):
            return it.words
    return None

def main(panel):
    pdir = os.path.join(r"E:\consoles", panel)
    dtb = os.path.join(pdir, [x for x in os.listdir(pdir) if x.endswith('.dtb')][0])
    f = load(dtb)
    root = f.get_rootnode()
    def walk(n):
        yield n
        for s in n.subdata:
            if isinstance(s,FdtNode): yield from walk(s)
    phmap={}
    for n in walk(root):
        for it in n.subdata:
            if isinstance(it,FdtProperty) and it.get_name()=='phandle':
                try: phmap[it.words[0]]=n.get_name()
                except: pass
    # find all panel nodes
    for n in walk(root):
        if isinstance(n,FdtNode) and ('panel' in n.get_name()):
            compat=[it.strings for it in n.subdata if isinstance(it,FdtProperty) and it.get_name()=='compatible']
            init=None
            for it in n.subdata:
                if isinstance(it,FdtProperty) and it.get_name()=='panel-init-sequence' and hasattr(it,'bytes'):
                    init=len(it.bytes)
            res=prop_words(n,'reset-gpios'); en=prop_words(n,'enable-gpios'); pw=prop_words(n,'power-supply')
            def fmt(g):
                if not g or len(g)<3: return str(g)
                return "%s pin%d flags%d"%(phmap.get(g[0],'ph%d'%g[0]), g[1], g[2])
            print(f"[{panel}] node={n.get_name()} compat={compat} init={init}B reset={fmt(res)} enable={fmt(en)} power={fmt(pw) if pw else None}")

for panel in ['k36s','k36','r36t','rx6h']:
    try:
        main(panel)
    except Exception as e:
        print(f"[{panel}] ERR {repr(e)}")
