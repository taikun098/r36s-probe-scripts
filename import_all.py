import os, shutil, time
src=r'D:\R36S_backup_20261018\EASYROMS'
dst='\\\\?\\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\\'
exclude={'psp','psx','pspminis','ports','ports_scripts','System Volume Information','videos','movies'}
log=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\import_log.txt'
start=time.time()
copied=0
with open(log,'w',encoding='utf-8') as lf:
    lf.write('start %s\n'%time.strftime('%H:%M:%S'))
    for e in os.listdir(src):
        if e in exclude:
            lf.write('skip %s\n'%e); continue
        s=os.path.join(src,e); d=os.path.join(dst,e)
        try:
            if os.path.isdir(s):
                shutil.copytree(s,d,dirs_exist_ok=True)
            else:
                os.makedirs(dst,exist_ok=True)
                shutil.copy2(s,os.path.join(dst,e))
            copied+=1
            lf.write('OK %s\n'%e)
        except Exception as ex:
            lf.write('ERR %s: %r\n'%(e,ex))
    lf.write('DONE copied=%d time=%.1fmin\n'%(copied,(time.time()-start)/60))
