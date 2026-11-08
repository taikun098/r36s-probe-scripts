import paramiko, io
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
# 更新启动脚本
script='''#!/bin/bash
cd /roms/ports/Half-Life
export LD_LIBRARY_PATH=.
export XASH3D_REFERENCE=gl4es
./xash3d -fullscreen -console -sdl_joy_old_api
'''
sf=c.open_sftp()
sf.putfo(io.BytesIO(script.encode()), '/tmp/HL.sh')
out,err=run(S+f'cp -f /tmp/HL.sh /mnt/roms/ports/Half-Life.sh; chmod +x /mnt/roms/ports/Half-Life.sh; echo 脚本更新=$?')
print(out if out else err)
print('\n=== 新启动脚本 ===')
out,err=run(S+'cat /mnt/roms/ports/Half-Life.sh 2>&1')
print(out if out else err)
print('\n=== 验证替换后引擎 ===')
out,err=run(S+f'ls -la {HL}/xash3d {HL}/libxash.so {HL}/libref_gl4es.so 2>&1')
print(out if out else err)
print('\n=== 半条命目录总览 ===')
out,err=run(S+f'ls -la {HL}/ 2>&1')
print(out if out else err)
c.close()
