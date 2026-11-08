import os
p=r"D:\R36S_backup_20261015\darkos"
log=os.path.join(p,"aria2_bt3.log")
out=[]
if os.path.exists(log):
    c=open(log,encoding='utf-8',errors='ignore').read()
    lines=c.splitlines()
    # last summary-like lines
    tail=[l for l in lines if any(x in l for x in ['B/', 'CN', 'seeding', 'DHT', 'DL:', 'error', 'Error', 'EXCEPTION', 'connecting'])]
    out.append("=== last 20 progress lines ===")
    out.append("\n".join(tail[-20:]))
else: out.append("(missing)")
out.append("=== file ===")
fp=os.path.join(p,"dArkOS_G80CA-RE_trixie_02062026.7z")
out.append("  size %d"%(os.path.getsize(fp) if os.path.exists(fp) else -1))
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\bt3_check.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
