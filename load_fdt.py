from pyfdt.pyfdt import FdtBlobParse
import inspect

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(path):
    with open(path, 'rb') as fh:
        return FdtBlobParse(fh).to_fdt()

print("walk sig:", inspect.signature(FdtBlobParse))
print("FdtBlobParse methods:", [x for x in dir(FdtBlobParse) if not x.startswith('_')])

f_ark = load(base + r"\origin_p1.dtb")
print("ark root:", f_ark.get_rootnode().get_name())
# resolve dsi panel path
for path in ['/dsi@ff450000', '/dsi@ff450000/panel@0']:
    try:
        node = f_ark.resolve_path(path)
        print("resolved", path, "->", node, type(node))
    except Exception as e:
        print("resolve err", path, e)
