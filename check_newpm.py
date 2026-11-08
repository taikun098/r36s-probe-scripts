import os, zipfile
out=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\newpm.txt"
L=[]
f=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\PortMaster_new.zip"
L.append("file exists: %s"%os.path.exists(f))
if os.path.exists(f):
    L.append("size: %d"%os.path.getsize(f))
    try:
        zf=zipfile.ZipFile(f)
        names=zf.namelist()
        L.append("zip entries: %d"%len(names))
        for kw in ['mod_ArkOS','mod_','control.txt','device_info','funcs','PortMaster.sh']:
            hits=[n for n in names if kw in n]
            L.append("=== %s: %d"%(kw,len(hits)))
            for h in hits[:15]: L.append("   "+h)
        # extract mod_ArkOS to working dir
        for n in names:
            if n.endswith('mod_ArkOS.txt') or n=='PortMaster/mod_ArkOS.txt':
                zf.extract(n, r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\newpm_extract")
                L.append("extracted: "+n)
    except Exception as e:
        L.append("zip err: "+str(e))
open(out,"w",encoding='utf-8').write("\n".join(L))
print("written",len(L),"lines")
