import os
bk=r'D:\R36S_backup_20261018\EASYROMS'
out=[]
try:
    entries=os.listdir(bk)
    out.append('total entries: %d' % len(entries))
    for e in entries:
        p=os.path.join(bk,e)
        if os.path.isdir(p):
            out.append('[dir]  '+e)
        else:
            out.append('[file] '+e+'  '+str(os.path.getsize(p)))
except Exception as ex:
    out.append('ERR %r' % ex)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\bk_list.txt'
open(r,'w').write('\n'.join(out))
print('done')
