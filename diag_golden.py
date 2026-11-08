import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
script = r'''
#!/bin/bash
set +e
echo "=== 1. 找光明之魂 ROM ==="
find /mnt/roms -maxdepth 3 -iname "*光明*" -o -maxdepth 3 -iname "*shining*soul*" 2>/dev/null
echo "--- gba 目录 ---"
ls /mnt/roms/gba/ 2>&1 | head -20
echo "--- 收藏夹/其他目录找光明 ---"
find /mnt/roms -iname "*光明之魂*" 2>/dev/null | head

echo ""
echo "=== 2. 找 mGBA 相关目录与金手指 ==="
find /mnt/roms -maxdepth 4 -iname "*mgba*" -o -maxdepth 4 -iname "*cheat*" -o -maxdepth 4 -iname "*MGB*" 2>/dev/null | head -30
echo "--- 系统分区找 mgba/cheat ---"
find /mnt/r36s -maxdepth 5 -iname "*mgba*" -o -maxdepth 5 -iname "*cheat*" 2>/dev/null | head -20

echo ""
echo "=== 3. gba 模拟器核心/存档相关 ==="
find /mnt/roms -maxdepth 2 -type d -iname "*gba*" 2>/dev/null
find /mnt/r36s -maxdepth 6 -type d -iname "*mgba*" 2>/dev/null | head
'''
with sftp.open('/tmp/diag_golden.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/diag_golden.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
