import os, re
out=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\diag_report.txt"
L=[]
p=r"E:\ports"
if os.path.isdir(p):
    sh=[f for f in os.listdir(p) if f.endswith('.sh')]
    dirs=[d for d in os.listdir(p) if os.path.isdir(os.path.join(p,d))]
    L.append("E:\\ports root .sh count: %d"%len(sh))
    L.append("E:\\ports subdir (game data) count: %d"%len(dirs))
    g=p+os.sep+"gamelist.xml"
    if os.path.exists(g):
        gx=open(g,encoding='utf-8').read()
        L.append("gamelist.xml <game> entries: %d"%gx.count("<game>"))
    else:
        L.append("gamelist.xml MISSING")
    L.append("E:\\ports\\PortMaster exists: %s"%os.path.isdir(p+os.sep+"PortMaster"))
    if os.path.isdir(p+os.sep+"PortMaster"):
        L.append("  PortMaster entries: %d"%len(os.listdir(p+os.sep+"PortMaster")))
else:
    L.append("E:\\ports MISSING")
# read 2048 game-dir script (full) and root 2048.sh
for f,tag in [(r"E:\ports\2048\2048.sh","GAME-DIR 2048.sh (FULL)"),(r"E:\ports\2048.sh","ROOT 2048.sh")]:
    if os.path.exists(f):
        c=open(f,encoding='utf-8',errors='replace').read()
        L.append("="*20+tag+"="*20)
        L.append(c)
    else:
        L.append("%s MISSING"%f)
# list 2048 data dir
d=r"E:\ports\2048"
if os.path.isdir(d):
    L.append("=== 2048 dir contents ===")
    for n in sorted(os.listdir(d)):
        fp=os.path.join(d,n)
        L.append("  %s (%s)"%(n, os.path.getsize(fp) if os.path.isfile(fp) else "dir"))
open(out,"w",encoding='utf-8').write("\n".join(L))
print("written",out,len(L),"lines")
