import os
p=r"D:\R36S_backup_20261015\darkos"
out=[]
for e in sorted(os.listdir(p)):
    fp=os.path.join(p,e)
    sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
    out.append("  %s %d bytes"%(e,sz) if sz else "  %s (dir)"%e)
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\dl_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
