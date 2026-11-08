import os
bk=r'D:\R36S_backup_20261018\EASYROMS\ports'
targets=['Battle for Wesnoth','Marathon','OpenXcomEX']
dirs=os.listdir(bk)
out=[]
for d in sorted(dirs):
    dl=d.lower()
    if any(t.lower() in dl for t in targets) or ('marathon' in dl):
        out.append(d)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\missing_ports.txt'
open(r,'w',encoding='utf-8').write('\n'.join(out) if out else 'NONE')
print('done')
