import os
bk=r'D:\R36S_backup_20261018\EASYROMS'
targets=['psp','psx','pspminis','ports','ports_scripts','arcade','gba','nes','snes','megadrive','genesis','mame','fbneo','neogeo','ps1','nds','n64','gamerom','themes','tools']
def dsize(p):
    sz=0;n=0
    for r,_,fs in os.walk(p):
        for f in fs:
            try:
                sz+=os.path.getsize(os.path.join(r,f)); n+=1
            except: pass
    return sz,n
out=[]
# top-level totals
tot=0
for e in os.listdir(bk):
    p=os.path.join(bk,e)
    if os.path.isdir(p):
        sz,n=dsize(p)
        tot+=sz
        if e in targets or sz>1e8:
            out.append('%s\t%.2f GB\t%d' % (e, sz/1e9, n))
out.append('TOTAL\t%.2f GB' % (tot/1e9))
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\bk_sizes.txt'
open(r,'w').write('\n'.join(out))
print('done')
