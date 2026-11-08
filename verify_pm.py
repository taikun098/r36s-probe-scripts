import os
print("E:\\ports\\PortMaster exists:", os.path.isdir(r"E:\ports\PortMaster"))
if os.path.isdir(r"E:\ports\PortMaster"):
    n=os.listdir(r"E:\ports\PortMaster"); print("  entries:",len(n)); print("  sample:",n[:20])
print("E:\\tools\\PortMaster exists:", os.path.isdir(r"E:\tools\PortMaster"))
c=open(r"E:\ports\PortMaster\control.txt",encoding='utf-8',errors='replace').read()
print("get_controls in control.txt:", "get_controls" in c)
print("mod_ArkOS exists:", os.path.exists(r"E:\ports\PortMaster\mod_ArkOS.txt"))
print("mod_.txt exists:", os.path.exists(r"E:\ports\PortMaster\mod_.txt"))
print("libs dir:", os.path.isdir(r"E:\ports\PortMaster\libs"), os.listdir(r"E:\ports\PortMaster\libs") if os.path.isdir(r"E:\ports\PortMaster\libs") else "N/A")
