import os, time
p=r"D:\R36S_backup_20261015\darkos"
fp=os.path.join(p,"dArkOS_enc.bin")
log=os.path.join(p,"aria2_cdn.log")
now=time.time()
out=[]
if os.path.exists(log):
    c=open(log,encoding='utf-8',errors='ignore').read()
    lines=[l for l in c.splitlines() if 'B(' in l or 'DL:' in l or 'error' in l.lower() or 'Error' in l or 'EXCEPTION' in l]
    out.append("=== progress tail ===")
    out.append("\n".join(lines[-6:]))
if os.path.exists(fp):
    sz=os.path.getsize(fp); age=now-os.path.getmtime(fp)
    out.append("=== dArkOS_enc.bin: %d bytes (%.2f GB) lastwrite %.0fs ago ==="%(sz,sz/1e9,age))
else:
    out.append("=== enc.bin missing ===")
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\cdn_check.txt","w",encoding="utf-8").write("\n".join(out))
print("\n".join(out))
