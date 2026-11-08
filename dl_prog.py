import os
p=r"D:\R36S_backup_20261015\darkos"
out=[]
for e in sorted(os.listdir(p)):
    fp=os.path.join(p,e)
    try:
        sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
    except: sz=-1
    out.append("  %s %d bytes"%(e,sz) if sz else "  %s (dir)"%e)
for log in ["aria2_bt.log"]:
    fp=os.path.join(p,log)
    out.append("=== %s tail ==="%log)
    if os.path.exists(fp):
        try:
            out.append(open(fp,encoding='utf-8',errors='ignore').read()[-1500:])
        except Exception as e: out.append("err %r"%e)
    else: out.append("(missing)")
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\dl_prog.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
