from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(p):
    return FdtBlobParse(open(p,'rb')).to_fdt()

def find_node_by_phandle(root, ph):
    for n in walk_all(root):
        for it in n.subdata:
            if isinstance(it,FdtProperty) and it.get_name()=='phandle':
                try:
                    if it.words[0]==ph: return n
                except: pass
    return None

def walk_all(node):
    yield node
    for s in node.subdata:
        if isinstance(s, FdtNode):
            yield from walk_all(s)

def phandle_of(node):
    for it in node.subdata:
        if isinstance(it,FdtProperty) and it.get_name()=='phandle':
            return it.words[0]
    return None

def resolve_gpio(f, gpios, label):
    if len(gpios)>=3:
        ph,pin,flags = gpios[0],gpios[1],gpios[2]
        node = find_node_by_phandle(f.get_rootnode(), ph)
        print("  %s: phandle=%d pin=%d flags=%d -> node=%s path=%s" % (label, ph, pin, flags, node.get_name() if node else None, node.path if hasattr(node,'path') else '?'))
    else:
        print("  %s: gpios=%s (short)" % (label, gpios))

for tag,path in [("clone type1 panel2", r"E:\consoles\clone type1 panel2\rk3326-r36s-type1-panel2-linux.dtb"), ("ORIG evb", base+r"\evb_orig.dtb")]:
    f = load(path)
    p = f.resolve_path('/dsi@ff450000/panel@0')
    print("="*30, tag)
    for it in p.subdata:
        if isinstance(it,FdtProperty):
            if it.get_name() in ('reset-gpios','enable-gpios','power-supply','backlight'):
                v = it.words if hasattr(it,'words') else None
                resolve_gpio(f, v, it.get_name())
    # also dsi reset/backlight context? skip
    print()
