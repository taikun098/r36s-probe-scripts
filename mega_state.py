import os, subprocess
# check mega log fresh
p=r"D:\R36S_backup_20261015\darkos"
log=os.path.join(p,"mega_dl.log")
out=[]
out.append("mega log size: %d"%(os.path.getsize(log) if os.path.exists(log) else -1))
out.append("=== mega log ===")
if os.path.exists(log):
    out.append(open(log,encoding='utf-8',errors='ignore').read())
# check python processes
out.append("=== python procs ===")
r=subprocess.run(['tasklist','/FI','IMAGENAME eq python.exe','/FO','CSV','/NH'],capture_output=True,text=True)
out.append(r.stdout[:1500])
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\mega_state.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
