import os, shutil, time
bk=r'D:\R36S_backup_20261018\EASYROMS\ports'
dst=r'\\?\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\ports'
log=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\import_ports_log.txt'
os.makedirs(dst,exist_ok=True)
lines=[]
# 1. PortMaster runtime
try:
    if os.path.isdir(os.path.join(bk,'PortMaster')):
        shutil.copytree(os.path.join(bk,'PortMaster'), os.path.join(dst,'PortMaster'), dirs_exist_ok=True)
        lines.append('PortMaster OK')
    else:
        lines.append('PortMaster MISSING in backup')
except Exception as e:
    lines.append('PortMaster ERR %r'%e)
# 2. gamelist.xml
try:
    if os.path.exists(os.path.join(bk,'gamelist.xml')):
        shutil.copy2(os.path.join(bk,'gamelist.xml'), os.path.join(dst,'gamelist.xml'))
        lines.append('gamelist.xml OK')
except Exception as e:
    lines.append('gamelist ERR %r'%e)
# 3. selected .sh + matching game dirs
shs=[f for f in os.listdir(bk) if f.endswith('.sh')]
bkdirs={d:os.path.join(bk,d) for d in os.listdir(bk) if os.path.isdir(os.path.join(bk,d))}
ok_dirs=0; miss_dirs=[]
for sh in sorted(shs):
    name=os.path.splitext(sh)[0]
    try:
        shutil.copy2(os.path.join(bk,sh), os.path.join(dst,sh))
    except Exception as e:
        lines.append('sh ERR %s %r'%(sh,e)); continue
    # find matching game data dir
    cands=[name, name.replace(' ',''), name.replace(' ','_'), name.replace(' ','-'), name.replace(' & ',' and ')]
    found=None
    for c in cands:
        if c in bkdirs:
            found=c; break
    if not found:
        # fuzzy: dir that starts with same first word
        first=name.split(' ')[0]
        for d in bkdirs:
            if d.lower()==name.lower() or d.lower().startswith(first.lower()):
                found=d; break
    if found:
        try:
            shutil.copytree(bkdirs[found], os.path.join(dst,found), dirs_exist_ok=True)
            ok_dirs+=1
        except Exception as e:
            lines.append('dir ERR %s %r'%(found,e))
    else:
        miss_dirs.append(name)
lines.append('selected .sh copied: %d'%len(shs))
lines.append('game dirs copied: %d'%ok_dirs)
lines.append('missing dirs (%d): %s'%(len(miss_dirs), ', '.join(miss_dirs[:20])))
open(log,'w',encoding='utf-8').write('\n'.join(lines))
print('ports import done')
