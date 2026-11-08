import sys
sys.path.insert(0, r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe")
import pyfdt
from pyfdt import PyFdt
p=r"L:\rk3326-g80ca-linux.dtb"
fdt=PyFdt.parse(open(p,'rb').read())
node=fdt.get_root()
def walk(n, prefix=""):
    for sub in n.subnodes:
        name=sub.name if hasattr(sub,'name') else sub
        if sub.name in ("model","compatible","panel"):
            print(prefix+sub.name, "=", sub.props.get("value") if hasattr(sub.props,'get') else "")
        walk(sub, prefix+sub.name+"/") if hasattr(sub,'subnodes') else None
# print root props
print("root props:", [ (p.name, getattr(p,'value',None)) for p in node.props ])
# walk compatible
for sub in node.subnodes:
    print("node:", sub.name)
    for prop in sub.props:
        if prop.name in ("compatible","model"):
            print("  ",prop.name,"=",prop.value)
