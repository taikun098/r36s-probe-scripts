import os, time
p=r"D:\R36S_backup_20261015\darkos"
out=[]
# mega log
for log in ["mega_dl2.log","mega_dl.log"]:
    fp=os.path.join(p,log)
    out.append("=== %s ==="%log)
    if os.path.exists(fp):
        out.append(open(fp,encoding='utf-8',errors='ignore').read()[-1200:])
    else: out.append("(missing)")
# any growing files
out.append("=== files with recent mtime ===")
now=time.time()
for e in sorted(os.listdir(p)):
    fp=os.path.join(p,e)
    if os.path.isfile(fp):
        try:
            sz=os.path.getsize(fp); mt=os.path.getmtime(fp)
            age=now-mt
            if sz>100000 or 'mega' in e.lower() or '.7z' in e.lower():
                out.append("  %s %d bytes age=%.0fs"%(e,sz,age))
        except: pass
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\mega_prog2.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
