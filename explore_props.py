from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty
import inspect

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(path):
    with open(path, 'rb') as fh:
        return FdtBlobParse(fh).to_fdt()

f = load(base + r"\evb_orig.dtb")
p = f.resolve_path('/dsi@ff450000/panel@0')

print("FdtProperty methods:", [x for x in dir(FdtProperty) if not x.startswith('_')])
print()
for item in p.subdata:
    if isinstance(item, FdtProperty):
        print("PROP", item.get_name(), "| type:", type(item).__name__, "| dict:", {k: (v if not isinstance(v,(bytes,list,str)) else (v[:60] if isinstance(v,(bytes,str)) else [type(x).__name__ for x in v])) for k,v in item.__dict__.items()})
