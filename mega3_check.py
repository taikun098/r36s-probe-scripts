import os, time
p=r"D:\R36S_backup_20261015\darkos"
out=[]
for log in ["mega_dl3.log"]:
    fp=os.path.join(p,log)
    out.append("=== %s ==="%log)
    if os.path.exists(fp):
        out.append(open(fp,encoding='utf-8',errors='ignore').read()[-1500:])
    else: out.append("(missing)")
out.append("=== file sizes ===")
now=time.time()
for e in sorted(os.listdir(p)):
    fp=os.path.join(p,e)
    if os.path.isfile(fp) and ('7z' in e or 'mega' in e):
        try:
            sz=os.path.getsize(fp); mt=os.path.getmtime(fp)
            out.append("  %s %d bytes age=%.0fs"%(e,sz,now-mt))
        except: pass
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\mega3_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
