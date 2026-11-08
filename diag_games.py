import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
script = r'''
#!/bin/bash
set +e
echo "=== 1. 土豆兄弟 runtime 检查 ==="
echo "--- 游戏分区 PortMaster/libs ---"
ls -la /mnt/roms/ports/PortMaster/libs/ 2>&1
echo "--- 系统分区 /opt/system/Tools/PortMaster/libs ---"
ls -la /mnt/r36s/opt/system/Tools/PortMaster/libs/ 2>&1
echo "--- brotato 目录 ---"
ls -la /mnt/roms/ports/brotatond/ 2>&1
ls -la /mnt/roms/ports/brotatond/gamedata/ 2>&1 | head

echo ""
echo "=== 2. Half-Life 目录检查 ==="
ls -la /mnt/roms/ports/Half-Life/ 2>&1
echo "--- xash3d ---"
ls -la /mnt/roms/ports/Half-Life/xash3d* 2>&1
echo "--- valve 目录 ---"
ls -la /mnt/roms/ports/Half-Life/valve/ 2>&1 | head
echo "--- 压缩包 ---"
find /mnt/roms/ports/Half-Life -maxdepth 1 -iname "*.zip" 2>/dev/null

echo ""
echo "=== 3. 火炬之光 loader 检查 ==="
ls -la /mnt/roms/ports/torchlight/ 2>&1 | head -20
echo "--- loader 库检查 ---"
find /mnt/roms/ports/torchlight -name "*.so*" 2>/dev/null | head

echo ""
echo "=== 4. vanillatd 检查 ==="
ls -la /mnt/roms/ports/vanillatd/ 2>&1 | head -20
echo "--- 找 vanillatd.aarch64 ---"
find /mnt/roms/ports/vanillatd -name "*.aarch64" 2>/dev/null

echo ""
echo "=== 5. 系统分区现有 PortMaster 结构 ==="
ls -la /mnt/r36s/opt/system/Tools/PortMaster/ 2>&1
'''
with sftp.open('/tmp/diag_games.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/diag_games.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
