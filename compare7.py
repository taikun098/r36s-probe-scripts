from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import glob, os

panels = ['clone type1 panel2','clone type1 panel5','clone type2 panel2','k36s','r36t','rx6h','sauce panel4']
base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(p):
    return FdtBlobParse(open(p,'rb')).to_fdt()

def prop_words(node,name):
    for it in node.subdata:
        if isinstance(it,FdtProperty) and it.get_name()==name and hasattr(it,'words'):
            return it.words
    return None

def resolve_ph(root, ph):
    from pyfdt.pyfdt import FdtNode
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
    if n is None: return "?"
    return n.get_name()

for panel in panels:
    pdir = os.path.join(r"E:\consoles", panel)
    dtb = os.path.join(pdir, [x for x in os.listdir(pdir) if x.endswith('.dtb')][0])
    f = load(dtb)
    p = f.resolve_path('/dsi@ff450000/panel@0')
    compat = [it.strings for it in p.subdata if isinstance(it,FdtProperty) and it.get_name()=='compatible']
    back = prop_words(p,'backlight')
    power = prop_words(p,'power-supply')
    enable = prop_words(p,'enable-gpios')
    reset = prop_words(p,'reset-gpios')
    def fmt_gpio(g):
        if not g: return None
        if len(g)>=3: return "bank=%s pin=%d flags=%d" % (gpiobank(f.get_rootnode(),g[0]), g[1], g[2])
        return g
    print("==== %s ====" % panel)
    print("  compatible:", compat)
    print("  backlight:", back)
    print("  power-supply:", power)
    print("  enable-gpios:", fmt_gpio(enable))
    print("  reset-gpios:", fmt_gpio(reset))
