import os
for bk in [r'D:\R36S_backup_20261015\EEROMS', r'D:\R36S_backup_20261015']:
    out=['BACKUP: '+bk]
    if not os.path.isdir(bk):
        out.append('  NOT PRESENT')
        continue
    try:
        entries=os.listdir(bk)
        out.append('  top entries: %d' % len(entries))
        for core in ['nes','snes','megadrive','genesis','gba','gbc','gb','n64','nds','psx','psp','arcade','neogeo','ports']:
            p=os.path.join(bk,core)
            if os.path.isdir(p):
                sz=0;n=0
                for r,_,fs in os.walk(p):
                    for f in fs:
                        try: sz+=os.path.getsize(os.path.join(r,f)); n+=1
                        except: pass
                out.append('  %s\t%.2f GB\t%d' % (core, sz/1e9, n))
            else:
                out.append('  %s\t(missing)' % core)
    except Exception as ex:
        out.append('  ERR %r' % ex)
    r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\eeroms_check.txt'
    open(r,'a').write('\n'.join(out)+'\n\n')
print('done')
