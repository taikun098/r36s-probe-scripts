import os
p=r"D:\R36S_backup_20261015\darkos"
log=os.path.join(p,"aria2_bt2.log")
out=[]
out.append("=== aria2_bt2.log tail ===")
if os.path.exists(log):
    c=open(log,encoding='utf-8',errors='ignore').read()
    # find latest summary lines
    lines=[l for l in c.splitlines() if 'B/' in l or 'CN' in l or 'Download' in l or 'connected' in l.lower() or 'EXCEPTION' in l or 'error' in l.lower()]
    out.append(c[-1800:])
else: out.append("(missing)")
out.append("=== files ===")
for e in sorted(os.listdir(p)):
    if 'G80CA-RE_trixie' in e or 'aria2' in e.lower():
        fp=os.path.join(p,e)
        try: sz=os.path.getsize(fp)
        except: sz=-1
        out.append("  %s %d"%(e,sz))
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\bt2_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
