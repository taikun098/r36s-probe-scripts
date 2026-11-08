import os
p=r"D:\R36S_backup_20261015\darkos"
log=os.path.join(p,"aria2_od.log")
out=[]
out.append("=== aria2_od.log tail ===")
if os.path.exists(log):
    c=open(log,encoding='utf-8',errors='ignore').read()
    out.append(c[-1500:])
else:
    out.append("(missing)")
# files
out.append("=== dir ===")
for e in sorted(os.listdir(p)):
    fp=os.path.join(p,e)
    try: sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
    except: sz=-1
    out.append("  %s %d"%(e,sz) if sz else "  %s (dir)"%e)
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\od_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
