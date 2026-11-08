import os
out=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\pm_files.txt"
L=[]
pm=r"E:\ports\PortMaster"
L.append("=== E:\\ports\\PortMaster full listing ===")
for n in sorted(os.listdir(pm)):
    fp=os.path.join(pm,n)
    L.append("  %s  (%s)"%(n,"dir" if os.path.isdir(fp) else os.path.getsize(fp)))
L.append("")
L.append("=== required files check ===")
req=["control.txt","device_info.txt","funcs.txt","gptokeyb","gptokeyb2","mapper.py","gamecontrollerdb.txt","libinterpose.aarch64.so","libinterpose.armhf.so","PortMaster.sh","mod_.txt","mod_ArkOS.txt"]
for r in req:
    L.append("  %-28s %s"%(r, "OK" if os.path.exists(os.path.join(pm,r)) else "MISSING"))
L.append("")
L.append("=== device_info.txt ===")
di=os.path.join(pm,"device_info.txt")
if os.path.exists(di):
    L.append(open(di,encoding='utf-8',errors='replace').read())
else:
    L.append("MISSING")
open(out,"w",encoding='utf-8').write("\n".join(L))
print("written",len(L),"lines")
