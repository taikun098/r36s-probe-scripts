import re, os
cfg=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\darkos_es_systems.cfg"
xml=open(cfg,encoding='utf-8').read()
# name -> (path, extension set lowercase)
sysinfo={}
for m in re.finditer(r'<system>(.*?)</system>', xml, re.S):
    blk=m.group(1)
    name=re.search(r'<name>(.*?)</name>',blk,re.S)
    path=re.search(r'<path>(.*?)</path>',blk,re.S)
    ext=re.search(r'<extension>(.*?)</extension>',blk,re.S)
    if not name: continue
    nm=name.group(1).strip()
    exts=set(e.lower() for e in ext.group(1).split()) if ext else set()
    sysinfo[nm]=(path.group(1).strip() if path else '', exts)

edir="E:\\"
print("System        expected-extensions                actual-dir-has-files?  sample-exts")
print("-"*110)
# check each system dir on E:
for nm,(path,exts) in sorted(sysinfo.items()):
    # get dir name from /roms/<x>/ ; handle nested like pico-8/carts
    rel=path.replace('/roms/','').strip('/')
    d=os.path.join(edir, rel.replace('/','\\'))
    if not os.path.isdir(d):
        continue
    # sample up to 6 files, collect extensions
    fexts=set()
    nfiles=0
    try:
        for dp,ds,fs in os.walk(d):
            for f in fs[:4000]:
                if os.path.getsize(os.path.join(dp,f))==0: continue
                nfiles+=1
                ext=os.path.splitext(f)[1].lower()
                if ext: fexts.add(ext)
            if nfiles>6: break
    except Exception:
        continue
    if nfiles==0:
        continue
    match=len(fexts & exts)
    flag = "" if match>0 else "  <-- NO MATCH"
    print("%-14s %-30s %-6s files ext=%s%s"%(nm, ",".join(sorted(exts))[:30], nfiles, ",".join(sorted(fexts))[:30], flag))
