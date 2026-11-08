import os
p=r"D:\R36S_backup_20261015\darkos"
log=os.path.join(p,"aria2_od2.log")
out=[]
out.append("=== aria2_od2.log ===")
if os.path.exists(log):
    c=open(log,encoding='utf-8',errors='ignore').read()
    out.append(c[-2000:])
else: out.append("(missing)")
# check files for progress
out.append("=== dir files ===")
for e in sorted(os.listdir(p)):
    if 'od2' in e or 'dArkOS' in e:
        fp=os.path.join(p,e)
        try: sz=os.path.getsize(fp)
        except: sz=-1
        out.append("  %s %d"%(e,sz))
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\od2_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
