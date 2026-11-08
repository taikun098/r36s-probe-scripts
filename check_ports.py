import os
ports=r'D:\R36S_backup_20261018\EASYROMS\ports'
out=[]
try:
    sh=[f for f in os.listdir(ports) if f.endswith('.sh')]
    dirs=[d for d in os.listdir(ports) if os.path.isdir(os.path.join(ports,d))]
    out.append('root .sh count: %d'%len(sh))
    out.append('root dirs count: %d'%len(dirs))
    out.append('--- root .sh (first 70) ---')
    for f in sorted(sh)[:70]:
        out.append('  '+f)
    out.append('--- PortMaster present: %s'%os.path.isdir(os.path.join(ports,'PortMaster')))
    out.append('--- gamelist present: %s'%os.path.exists(os.path.join(ports,'gamelist.xml')))
except Exception as ex:
    out.append('ERR %r'%ex)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\ports_struct.txt'
open(r,'w',encoding='utf-8').write('\n'.join(out))
print('done')
