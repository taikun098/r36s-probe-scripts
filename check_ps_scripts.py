import os, re
ps=r"E:\ports_scripts"
portsdir=r"E:\ports"
scripts=[f for f in os.listdir(ps) if f.endswith('.sh')]
print("ports_scripts .sh count:",len(scripts))
ok=0; bad=[]
for f in scripts:
    path=os.path.join(ps,f)
    try:
        content=open(path,encoding='utf-8',errors='replace').read()
    except:
        bad.append((f,'read-err')); continue
    # GAME_DIR='...' or directory="..." lines
    m=re.search(r"GAME_DIR\s*=\s*['\"]([^'\"]+)['\"]", content)
    if not m:
        bad.append((f,'no-GAMEDIR')); continue
    gd=m.group(1)
    # map /roms/ports/X -> E:\ports\X
    gm=re.search(r"/roms/ports/(.+)$", gd)
    if not gm:
        bad.append((f,'bad-path:'+gd)); continue
    rel=gm.group(1)
    tgt=os.path.join(portsdir, rel)
    if os.path.exists(tgt):
        ok+=1
    else:
        bad.append((f,'missing:'+rel))
print("scripts whose target game dir exists:",ok)
print("problem scripts:",len(bad))
for b in bad[:20]:
    print("  ",b)
