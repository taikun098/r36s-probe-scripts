import zipfile, os
zf=zipfile.ZipFile(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\pm_extract\PortMaster.zip")
for dest in [r"E:\ports", r"E:\tools"]:
    zf.extractall(dest)
    print("extracted to",dest)
print("=== verify E:\\ports\\PortMaster ===")
for f in ["PortMaster.sh","control.txt","mod_.txt"]:
    p=os.path.join(r"E:\ports\PortMaster",f)
    print(f,"exists" if os.path.exists(p) else "MISSING")
print("=== control.txt head ===")
c=open(r"E:\ports\PortMaster\control.txt",encoding='utf-8',errors='replace').read()
print(c[:800])
