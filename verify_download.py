import os, urllib.request
# 1. verify Linux_Reader.exe PE header
p=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\tools\Linux_Reader.exe"
sz=os.path.getsize(p)
with open(p,'rb') as f: head=f.read(2)
print('Linux_Reader.exe:',sz,'B',head, 'PE' if head==b'MZ' else 'NOT-EXE')

# 2. re-download Ext4Fsd
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
url='https://github.com/bobranten/Ext4Fsd/releases/download/v0.71/Ext2Fsd-0.71-setup.exe'
out=os.path.join(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\tools",'Ext2Fsd-0.71-setup.exe')
try:
    r=opener.open(url,timeout=180)
    with open(out,'wb') as f:
        while True:
            chunk=r.read(1<<20)
            if not chunk: break
            f.write(chunk)
    sz2=os.path.getsize(out)
    print('Ext4Fsd downloaded:',sz2,'B = %.1fMB'%(sz2/1048576))
    with open(out,'rb') as f: print('head',f.read(2))
except Exception as e:
    print('ERR Ext4Fsd',repr(e))
print('DONE')
