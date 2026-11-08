from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty, FdtPropertyStrings

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"
src = r"E:\consoles\clone type1 panel2\rk3326-r36s-type1-panel2-linux.dtb"
f = FdtBlobParse(open(src,'rb')).to_fdt()
p = f.resolve_path('/dsi@ff450000/panel@0')
# change compatible to st7703 + simple-panel-dsi
new_sub = []
for it in p.subdata:
    if isinstance(it, FdtProperty) and it.get_name() == 'compatible':
        new_sub.append(FdtPropertyStrings('compatible', ['sitronix,st7703','simple-panel-dsi']))
    else:
        new_sub.append(it)
p.subdata = new_sub
out = base + r"\r36s_type1p2_st7703compat.dtb"
open(out,'wb').write(f.to_dtb())
print("written", out)
# verify
g = FdtBlobParse(open(out,'rb')).to_fdt()
gp = g.resolve_path('/dsi@ff450000/panel@0')
for it in gp.subdata:
    if isinstance(it,FdtProperty) and it.get_name()=='compatible':
        print("compatible:", it.strings)
