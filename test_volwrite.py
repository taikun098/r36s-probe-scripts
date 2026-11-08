import os, shutil, time
src=r'D:\R36S_backup_20261018\EASYROMS\arcade'
dst=r'\\?\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\arcade'
out=[]
try:
    os.makedirs(dst, exist_ok=True)
    n=0
    for f in os.listdir(src):
        s=os.path.join(src,f); d=os.path.join(dst,f)
        if os.path.isdir(s):
            shutil.copytree(s,d,dirs_exist_ok=True)
        else:
            shutil.copy2(s,d)
        n+=1
    out.append('arcade copied %d items'%n)
    # verify
    cnt=sum(len(fs) for _,_,fs in os.walk(dst))
    out.append('dest files: %d'%cnt)
except Exception as ex:
    out.append('ERR %r'%ex)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\volwrite_test.txt'
open(r,'w').write('\n'.join(out))
print('done')
