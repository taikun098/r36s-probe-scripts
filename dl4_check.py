import os, time
p=r"D:\R36S_backup_20261015\darkos"
fp=os.path.join(p,"dArkOS_G80CA-RE_trixie_02062026.7z")
log=os.path.join(p,"mega_dl4.log")
now=time.time()
out=[]
out.append("=== log tail ===")
if os.path.exists(log):
    out.append(open(log,encoding='utf-8',errors='ignore').read()[-600:])
else: out.append("(missing)")
if os.path.exists(fp):
    sz=os.path.getsize(fp); age=now-os.path.getmtime(fp)
    out.append("=== file: %d bytes (%.2f GB) lastwrite %.0fs ago ==="%(sz,sz/1e9,age))
else:
    out.append("=== file missing ===")
# temp file mega.py uses
temps=[e for e in os.listdir(p) if 'megapy' in e.lower() or e.lower().startswith('megapy')]
out.append("temps: %s"%temps)
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\dl4_check.txt","w",encoding="utf-8").write("\n".join(out))
print("\n".join(out))
