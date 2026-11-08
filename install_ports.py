import os, shutil, time
dst=r'G:\ports'
ex=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\extract_new'
log=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\install_ports_log.txt'
lines=[time.strftime('%H:%M:%S')+' start']
os.makedirs(dst,exist_ok=True)
# 1. copy new games
news={
 '土豆兄弟-新黎明.sh': os.path.join(ex,'土豆兄弟','土豆兄弟-新黎明.sh'),
 'brotatond': os.path.join(ex,'土豆兄弟','brotatond'),
 'Half-Life.sh': os.path.join(ex,'半条命','Half-Life.sh'),
 'Half-Life': os.path.join(ex,'半条命','Half-Life'),
 '火炬之光.sh': os.path.join(ex,'火炬之光','火炬之光.sh'),
 'torchlight': os.path.join(ex,'火炬之光','torchlight'),
 'Asphalt 6 Adrenaline.sh': os.path.join(ex,'狂野飙车6','Asphalt 6 Adrenaline.sh'),
 'asphalt6': os.path.join(ex,'狂野飙车6','asphalt6'),
}
for name,src in news.items():
    d=os.path.join(dst,name)
    try:
        if os.path.isdir(src):
            shutil.copytree(src,d,dirs_exist_ok=True)
        else:
            shutil.copy2(src,d)
        lines.append('COPY OK '+name)
    except Exception as e:
        lines.append('COPY ERR %s %r'%(name,str(e)[:120]))
# 2. keep sets
keep_sh={'OpenRA.sh','VanillaRA.sh','VanillaTD.sh','土豆兄弟-新黎明.sh','Half-Life.sh','火炬之光.sh','Asphalt 6 Adrenaline.sh'}
keep_dir={'openra','vanillara','vanillatd','PortMaster','brotatond','Half-Life','torchlight','asphalt6'}
# 3. delete non-kept
try:
    for e in os.listdir(dst):
        ep=os.path.join(dst,e)
        if e.endswith('.sh'):
            if e not in keep_sh:
                os.remove(ep); lines.append('DEL sh '+e)
        elif os.path.isdir(ep):
            if e not in keep_dir:
                shutil.rmtree(ep,ignore_errors=True); lines.append('DEL dir '+e)
except Exception as e:
    lines.append('DELETE ERR %r'%str(e)[:120])
# 4. rebuild gamelist
kept_sh=[f for f in os.listdir(dst) if f.endswith('.sh')]
gamelist=['<?xml version="1.0" encoding="UTF-8"?>','<gameList>']
for f in sorted(kept_sh):
    name=os.path.splitext(f)[0]
    gamelist.append('  <game>')
    gamelist.append('    <path>./%s</path>'%f)
    gamelist.append('    <name>%s</name>'%name)
    gamelist.append('    <desc></desc>')
    gamelist.append('  </game>')
gamelist.append('</gameList>')
open(os.path.join(dst,'gamelist.xml'),'w',encoding='utf-8').write('\n'.join(gamelist))
lines.append('gamelist rebuilt with %d games'%len(kept_sh))
lines.append('DONE')
open(log,'w',encoding='utf-8').write('\n'.join(lines))
print('done')
