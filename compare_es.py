import re, os
cfg=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\darkos_es_systems.cfg"
xml=open(cfg,encoding='utf-8').read()
# parse systems: name, path, extension
systems=[]
for m in re.finditer(r'<system>(.*?)</system>', xml, re.S):
    blk=m.group(1)
    name=re.search(r'<name>(.*?)</name>',blk,re.S)
    path=re.search(r'<path>(.*?)</path>',blk,re.S)
    ext=re.search(r'<extension>(.*?)</extension>',blk,re.S)
    if name:
        systems.append((name.group(1).strip(), path.group(1).strip() if path else '', ext.group(1).strip() if ext else ''))
print("total systems defined:",len(systems))
# print ports system
for n,p,e in systems:
    if n in ('ports','pico','pico-8','roms','tools'):
        print("SYSTEM %s path=%s ext=%s"%(n,p,e))
# collect expected dir names (basename of /roms/<x>/)
expdirs=set()
for n,p,e in systems:
    if p.startswith('/roms'):
        sub=p.replace('/roms/','').strip('/')
        if sub: expdirs.add(sub)
# list E:\ top-level
edir="E:\\"
actual=set(d for d in os.listdir(edir) if os.path.isdir(os.path.join(edir,d)))
print("\n=== E:\\ dirs NOT scanned by dArkOS (extra dirs) ===")
extra=sorted(actual-expdirs)
print("count:",len(extra))
for d in extra:
    print("  ",d)
print("\n=== expected dirs missing from E:\\ ===")
missing=sorted(expdirs-actual)
print("count:",len(missing))
for d in missing:
    print("  ",d)
