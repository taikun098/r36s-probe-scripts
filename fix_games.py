import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
script = r'''
#!/bin/bash
set +e
echo "=== 1. 修复土豆兄弟 runtime 位置 ==="
echo "--- 系统分区 PortMaster 目录 ---"
ls -la /mnt/r36s/opt/system/Tools/ 2>&1
echo "--- 创建 libs 并复制 runtime ---"
mkdir -p /mnt/r36s/opt/system/Tools/PortMaster/libs
cp /mnt/roms/ports/PortMaster/libs/frt_3.6.squashfs /mnt/r36s/opt/system/Tools/PortMaster/libs/
ls -la /mnt/r36s/opt/system/Tools/PortMaster/libs/
echo "--- 检查 PortMaster funcs.txt 引用路径 ---"
grep -rn "libs\|frt_3.6" /mnt/r36s/opt/system/Tools/PortMaster/*.txt /mnt/r36s/opt/system/Tools/PortMaster/*.sh 2>/dev/null | head

echo ""
echo "=== 2. 半条命 xash3d 文件类型 ==="
file /mnt/roms/ports/Half-Life/xash3d 2>&1
echo "--- xash3d 开头内容 ---"
head -c 200 /mnt/roms/ports/Half-Life/xash3d 2>&1 | xxd | head
echo ""
echo "--- 半条命启动脚本 ---"
cat /mnt/roms/ports/Half-Life.sh 2>&1

echo ""
echo "=== 3. 解压 valve 内容检查 ==="
echo "--- valve 目录顶层 ---"
ls /mnt/roms/ports/Half-Life/valve/ 2>&1
echo "--- 压缩包内容 ---"
unzip -l "/mnt/roms/ports/Half-Life/Copy Contents into valve folder.zip" 2>&1 | head -20
'''
with sftp.open('/tmp/fix_games.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/fix_games.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
