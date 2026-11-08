import os
p=r"D:\R36S_backup_20261015\darkos"
out=[]
if not os.path.isdir(p):
    out.append("dir missing")
else:
    for e in os.listdir(p):
        fp=os.path.join(p,e)
        sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
        out.append("  %s %d bytes"%(e,sz) if sz else "  %s (dir)"%e)
log=os.path.join(p,"mega_dl.log")
out.append("=== log exists: %s ==="%os.path.exists(log))
if os.path.exists(log):
    out.append(open(log,encoding='utf-8',errors='ignore').read()[-3000:])
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\mega_check_result.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
