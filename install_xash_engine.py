import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
S='echo 1 | sudo -S '
HL='/mnt/roms/ports/Half-Life'
SRC='/tmp/xash3d/xash3d-fwgs-linux-arm64'
print('=== 备份半条命目录 ===')
out,err=run(S+f'cp -r "{HL}" /mnt/roms/ports/Half-Life.bak_oldengine 2>&1; echo B=$?')
print(out if out else err)
print('\n=== 复制完整引擎文件 ===')
for f in ['xash3d','libxash.so','libref_gl.so','libref_gles1.so','libref_gles2.so','libref_gles3compat.so','libref_gl4es.so','libref_null.so','libmenu.so','libmenu_tui.so','filesystem_stdio.so','mdldec','xash','libSDL2-2.0.so','libSDL2-2.0.so.0','libSDL2-2.0.so.0.3200.10','libSDL2.so','activities.txt']:
    out,err=run(S+f'cp -f "{SRC}/{f}" "{HL}/" 2>&1; echo "$f=$?"')
    if '=0' in (out or ''):
        print(f'  ✓ {f}')
    else:
        print(f'  ✗ {f}: {out.strip()} {err.strip()}')
print('\n=== 复制 extras.pk3 到 valve ===')
out,err=run(S+f'cp -f "{SRC}/valve/extras.pk3" "{HL}/valve/" 2>&1; echo E=$?')
print(out if out else err)
c.close()
