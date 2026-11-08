import os, shutil
bk=r'D:\R36S_backup_20261018\EASYROMS\ports'
dst=r'\\?\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\ports'
lines=[]
for d in ['wesnoth','openxcom']:
    s=os.path.join(bk,d)
    if os.path.isdir(s):
        try:
            shutil.copytree(s, os.path.join(dst,d), dirs_exist_ok=True)
            lines.append('copied '+d)
        except Exception as e:
            lines.append('ERR %s %r'%(d,str(e)[:200]))
    else:
        lines.append('missing '+d)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\copy_wesnoth_log.txt'
open(r,'w',encoding='utf-8').write('\n'.join(lines))
print('done')
