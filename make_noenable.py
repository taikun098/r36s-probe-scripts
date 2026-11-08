from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"
src = r"E:\consoles\clone type1 panel2\rk3326-r36s-type1-panel2-linux.dtb"
f = FdtBlobParse(open(src,'rb')).to_fdt()
p = f.resolve_path('/dsi@ff450000/panel@0')
# remove enable-gpios
new_sub = [it for it in p.subdata if not (isinstance(it,FdtProperty) and it.get_name()=='enable-gpios')]
p.subdata = new_sub
out = base + r"\r36s_type1p2_noenable.dtb"
open(out,'wb').write(f.to_dtb())
print("written", out)
g = FdtBlobParse(open(out,'rb')).to_fdt()
gp = g.resolve_path('/dsi@ff450000/panel@0')
props=[it.get_name() for it in gp.subdata if isinstance(it,FdtProperty)]
print("enable-gpios present:", 'enable-gpios' in props)
