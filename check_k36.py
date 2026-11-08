from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import os

panels = ['k36s','k36','r36t','rx6h','clone type1 panel5','clone type1 panel5 invert','clone type2 panel2','r36xx','r36splus','r36pro']

def load(p): return FdtBlobParse(open(p,'rb')).to_fdt()
def prop_words(node,name):
    for it in node.subdata:
        if isinstance(it,FdtProperty) and it.get_name()==name and hasattr(it,'words'):
            return it.words
    return None

def resolve_ph(root, ph):
    def walk(n):
        yield n
        for s in n.subdata:
            if isinstance(s,FdtNode): yield from walk(s)
    for n in walk(root):
        for it in n.subdata:
            if isinstance(it,FdtProperty) and it.get_name()=='phandle':
                try:
                    if it.words[0]==ph: return n
                except: pass
    return None

def gpiobank(root, ph):
    n = resolve_ph(root, ph)
    return n.get_name() if n else "?"

for panel in panels:
    pdir = os.path.join(r"E:\consoles", panel)
    if not os.path.isdir(pdir):
        print(panel, ": MISSING"); continue
    dtb = os.path.join(pdir, [x for x in os.listdir(pdir) if x.endswith('.dtb')][0])
    try:
        f = load(dtb)
        p = f.resolve_path('/dsi@ff450000/panel@0')
        if p is None:
            print(panel, ": no panel@0"); continue
        compat=[]
        for it in p.subdata:
            if isinstance(it,FdtProperty) and it.get_name()=='compatible':
                compat=it.strings
        def gfmt(name):
            g=prop_words(p,name)
            if not g: return None
            if len(g)>=3: return f"{gpiobank(f.get_rootnode(),g[0])} pin{g[1]} flags{g[2]}"
            return str(g)
        # detect if st7703 via init bytes size
        init=None
        for it in p.subdata:
            if isinstance(it,FdtProperty) and it.get_name() in ('panel-init-sequence','panel-init-sequence-param') and hasattr(it,'bytes'):
                init=len(it.bytes)
        print(f"{panel}: compat={compat} init_bytes={init} reset={gfmt('reset-gpios')} enable={gfmt('enable-gpios')} power={prop_words(p,'power-supply')}")
    except Exception as e:
        print(panel, "ERR", repr(e))
