import os
p=r"D:\R36S_backup_20261015\darkos"
print("dir:", p)
try:
    for e in os.listdir(p):
        fp=os.path.join(p,e)
        sz=os.path.getsize(fp) if os.path.isfile(fp) else 0
        print("  ", e, "%d bytes"%(sz) if sz else "(dir)")
except Exception as ex:
    print("ERR", ex)
# log
log=os.path.join(p,"mega_dl.log")
if os.path.exists(log):
    print("=== mega_dl.log ===")
    print(open(log,encoding='utf-8',errors='ignore').read())
