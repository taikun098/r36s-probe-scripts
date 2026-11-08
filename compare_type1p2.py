from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(p):
    return FdtBlobParse(open(p,'rb')).to_fdt()

def show_props(node, label):
    print("  ["+label+"]")
    for it in node.subdata:
        if isinstance(it, FdtProperty):
            n = it.get_name()
            if hasattr(it,'strings'): v=it.strings
            elif hasattr(it,'words'): v=it.words
            elif hasattr(it,'bytes'): v='bytes[%d]'%len(it.bytes)
            else: v='?'
            print("    %-22s = %s" % (n, v))
    for it in node.subdata:
        if isinstance(it, FdtNode):
            show_props(it, it.get_name())

# clone type1 panel2
f1 = load(r"E:\consoles\clone type1 panel2\rk3326-r36s-type1-panel2-linux.dtb")
p1 = f1.resolve_path('/dsi@ff450000/panel@0')
print("=========== clone type1 panel2 ===========")
show_props(p1, "panel@0")

# orig
f2 = load(base + r"\evb_orig.dtb")
p2 = f2.resolve_path('/dsi@ff450000/panel@0')
print("=========== ORIG evb ===========")
show_props(p2, "panel@0")
