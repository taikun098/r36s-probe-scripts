import os
p=r"D:\R36S_backup_20261015\darkos"
for e in os.listdir(p):
    fp=os.path.join(p,e)
    sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
    print("  ", e, "%d bytes"%(sz) if sz else "(dir)")
log=os.path.join(p,"mega_dl.log")
if os.path.exists(log):
    print("=== log ===")
    print(open(log,encoding='utf-8',errors='ignore').read()[-2000:])
