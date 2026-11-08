from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"
src = r"E:\consoles\clone type1 panel2\rk3326-r36s-type1-panel2-linux.dtb"
f = FdtBlobParse(open(src,'rb')).to_fdt()

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

# panel@0 phandle
p = f.resolve_path('/dsi@ff450000/panel@0')
print("panel@0 phandle:", phandle_of(p))

# dsi node
dsi = f.resolve_path('/dsi@ff450000')
print("dsi@ff450000 props:")
for it in dsi.subdata:
    if isinstance(it,FdtProperty):
        n=it.get_name()
        v = it.strings if hasattr(it,'strings') else (it.words if hasattr(it,'words') else ('bytes[%d]'%len(it.bytes) if hasattr(it,'bytes') else '?'))
        print("   ", n, "=", v)
    if isinstance(it,FdtNode):
        print("   subnode:", it.get_name(), "phandle:", phandle_of(it))

# search for any node referencing panel phandle or named panel
pph = phandle_of(p)
print("searching refs to panel phandle", pph)
for n in walk_all(f.get_rootnode()):
    for it in n.subdata:
        if isinstance(it,FdtProperty):
            if it.get_name() in ('panel','remote-endpoint') and hasattr(it,'words'):
                if pph in it.words:
                    print("   ref in", n.get_name(), "prop", it.get_name(), "path", end=' ')
                    # get path
                    pth=[]
                    cur=n
                    while cur is not None and hasattr(cur,'parent'):
                        pth.insert(0,cur.get_name()); cur=cur.parent
                    print('/'.join(pth))
