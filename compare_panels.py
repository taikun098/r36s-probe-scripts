from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty, FdtPropertyStrings, FdtPropertyWords, FdtPropertyBytes
import copy

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(path):
    with open(path, 'rb') as fh:
        return FdtBlobParse(fh).to_fdt()

def get_prop(node, name):
    for item in node.subdata:
        if isinstance(item, FdtProperty) and item.get_name() == name:
            return item
    return None

def get_node(node, name):
    for item in node.subdata:
        if isinstance(item, FdtNode) and item.get_name() == name:
            return item
    return None

def timing_summary(tnode):
    out = {}
    for item in tnode.subdata:
        if isinstance(item, FdtProperty):
            out[item.get_name()] = item
    return out

for tag, path in [("ARKOS-origin_p1", base+r"\origin_p1.dtb"), ("ORIG-evb", base+r"\evb_orig.dtb")]:
    f = load(path)
    p = f.resolve_path('/dsi@ff450000/panel@0')
    compat = get_prop(p, 'compatible')
    init = get_prop(p, 'panel-init-sequence')
    exitp = get_prop(p, 'panel-exit-sequence')
    dt = get_node(p, 'display-timings')
    print("="*30, tag)
    if compat: print("  compatible:", compat.strings if hasattr(compat,'strings') else compat)
    if init:
        b = init.bytes if hasattr(init,'bytes') else None
        print("  init-seq len:", len(b) if b else init)
    if exitp:
        print("  exit-seq:", exitp.words if hasattr(exitp,'words') else exitp)
    if dt:
        print("  display-timings subnodes:", [s.get_name() for s in dt.subdata if isinstance(s,FdtNode)])
        for sub in dt.subdata:
            if isinstance(sub, FdtNode):
                print("   ["+sub.get_name()+"]", {pr.get_name(): pr.words if hasattr(pr,'words') else None for pr in sub.subdata if isinstance(pr,FdtProperty)})
    print()
