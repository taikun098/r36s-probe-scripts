import zipfile, os
base=r'C:\Users\user\Desktop\移植'
zips=['R36S-Ports管理器-v0.1.zip','半条命（中文）.zip','土豆兄弟-新黎明.zip','火炬之光测试.zip']
out=[]
for z in zips:
    p=os.path.join(base,z)
    out.append('='*60)
    out.append('FILE: '+z+'  ('+str(round(os.path.getsize(p)/1024/1024,1))+' MB)')
    try:
        zf=zipfile.ZipFile(p)
        names=zf.namelist()
        out.append('total entries: %d'%len(names))
        out.append('--- first 40 entries ---')
        for n in names[:40]:
            out.append('  '+n)
        # detect sh scripts
        shs=[n for n in names if n.lower().endswith('.sh') or n.lower().endswith('port.json') or n.lower().endswith('control.txt')]
        if shs:
            out.append('--- port-related files (%d) ---'%len(shs))
            for s in shs[:15]:
                out.append('  '+s)
    except Exception as e:
        out.append('ERR %r'%e)
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\desktop_ports.txt'
open(r,'w',encoding='utf-8').write('\n'.join(out))
print('done')
