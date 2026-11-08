from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import inspect

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(path):
    with open(path, 'rb') as fh:
        return FdtBlobParse(fh).to_fdt()

def prop_str(p):
    name = p.get_name()
    try:
        raw = p.to_raw()  # bytes
        return name, raw
    except Exception as e:
        return name, "<err>"

def dump_node(node, depth, maxdepth=5):
    print('  '*depth + node.get_name())
    if depth >= maxdepth:
        return
    d = node.__dict__
    # find subnodes and props
    for k, v in d.items():
        if isinstance(v, list):
            for item in v:
                if isinstance(item, FdtNode):
                    dump_node(item, depth+1, maxdepth)
                elif isinstance(item, FdtProperty):
                    print('  '* (depth+1) + "PROP " + item.get_name())
        elif isinstance(item if False else v, FdtNode):
            dump_node(v, depth+1, maxdepth)
        elif isinstance(v, FdtProperty):
            print('  '*(depth+1) + "PROP " + v.get_name())

print("FdtNode walk sig:", inspect.signature(FdtNode.walk))
print("FdtNode remove sig:", inspect.signature(FdtNode.remove))
print("FdtNode add_subnode sig:", inspect.signature(FdtNode.add_subnode))

for tag, path in [("ARKOS", base+r"\origin_p1.dtb"), ("ORIG", base+r"\evb_orig.dtb")]:
    f = load(path)
    pnode = f.resolve_path('/dsi@ff450000/panel@0')
    print("="*25, tag, "panel@0 __dict__ keys:", list(pnode.__dict__.keys()))
    dump_node(pnode, 0, 6)
    print()
