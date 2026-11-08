import urllib.request, os
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
outdir=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\tools"
os.makedirs(outdir,exist_ok=True)
jobs=[
 ('Linux_Reader.exe','https://eu.diskinternals.com/download/Linux_Reader.exe'),
 ('Ext2Fsd-0.71-setup.exe','https://github.com/bobranten/Ext4Fsd/releases/download/v0.71/Ext2Fsd-0.71-setup.exe'),
]
for name,url in jobs:
    path=os.path.join(outdir,name)
    try:
        print('下载',name,'...',flush=True)
        opener.open(url,timeout=120)
        urllib.request.urlretrieve(url,path)
        # re-download via urlretrieve with proxy? use opener direct
        sz=os.path.getsize(path)
        print('完成:',name,sz,'B = %.1fMB'%(sz/1048576),flush=True)
    except Exception as e:
        print('ERR',name,repr(e))
print('DONE')
