import os
bk=r"D:\R36S_backup_20261015\EEROMS"
e="E:\\"
# 不期望复制到 E:\ 的 EmuELEC 系统/媒体目录（已按同样清单排除）
excluded={".update","Alarms","Audiobooks","backup","bezels","BGM","DCIM","Documents",
"Download","downloads","LOST.DIR","Movies","Music","Notifications","Pictures","Podcasts",
"Recordings","Ringtones","screenshots","splash","savestates","tools","themes",
"System Volume Information","ports","ports_scripts","bgmusic"}

def count(p):
    n=0
    for dp,ds,fs in os.walk(p):
        n+=len(fs)
    return n

mism=[]
for d in sorted(os.listdir(bk)):
    if d in excluded: continue
    bdp=os.path.join(bk,d)
    if not os.path.isdir(bdp): continue
    edp=os.path.join(e,d)
    be=count(bdp)
    ee=count(edp) if os.path.isdir(edp) else -1
    if be!=ee:
        mism.append((d,be,ee))

print("checked top-level game dirs, mismatches:")
if not mism:
    print("  NONE - all match")
for d,b,x in mism:
    print("  %-14s backup=%d E:\\=%s"%(d,b,x))
