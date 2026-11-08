import os
base = r"D:\R36S_backup_20261015"
def ls(p, indent=""):
    try:
        for e in os.scandir(p):
            try:
                isd = e.is_dir()
                sz = "" if isd else ("%.2f MB" % (e.stat().st_size/1048576))
                print(indent + ("[D] " if isd else "    ") + e.name + ("  "+sz if sz else ""))
            except Exception as ex:
                print(indent, "?", e.name, ex)
    except Exception as ex:
        print("ERR", p, ex)
print("=== backup root ===")
ls(base)
for d in ["firmware","extract","EEROMS"]:
    p=os.path.join(base,d)
    if os.path.isdir(p):
        print("=== %s ===" % d)
        ls(p)
        # EEROMS just top level
print("=== EEROMS top-level entries (first 40) ===")
p=os.path.join(base,"EEROMS")
if os.path.isdir(p):
    n=0
    for e in os.scandir(p):
        if n<40:
            print(("  [D]" if e.is_dir() else "     ")+e.name)
        n+=1
    print("total entries:", n)
