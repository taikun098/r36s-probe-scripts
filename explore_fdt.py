import pyfdt.pyfdt as fdt
import sys

def dump_node(node, depth, maxdepth=6):
    name = getattr(node, 'name', str(node))
    print('  '*depth + name)
    if depth >= maxdepth:
        return
    # subnodes
    subs = node.subnodes if hasattr(node, 'subnodes') else []
    for s in subs:
        dump_node(s, depth+1, maxdepth)

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"
for tag, path in [("ARKOS-origin-p1", base+r"\origin_p1.dtb"), ("ORIGINAL-evb", base+r"\evb_orig.dtb")]:
    print("="*30, tag)
    blob = open(path, 'rb').read()
    f = fdt.Fdt.parse(blob)
    print("Fdt type:", type(f))
    print("attrs:", [a for a in dir(f) if not a.startswith('__')])
    # try to get root
    root = None
    for attr in ['root_node', 'root', 'tree']:
        if hasattr(f, attr):
            root = getattr(f, attr); print("root via", attr, type(root)); break
    if root is None:
        # walk to find
        try:
            f.walk(dump_node)
            continue
        except Exception as e:
            print("walk err", e)
    else:
        dump_node(root, 0)
    print()
