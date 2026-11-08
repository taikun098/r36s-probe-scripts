import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
# 用 python3 在服务器解压 valve.zip 到 valve 目录
script = r'''
#!/bin/bash
set +e
echo "=== 解压 Half-Life valve 压缩包 ==="
sudo -S python3 <<'PYEOF' << 'EOF'
import zipfile, os, sys
p="/mnt/roms/ports/Half-Life/Copy Contents into valve folder.zip"
dest="/mnt/roms/ports/Half-Life/valve"
try:
    z=zipfile.ZipFile(p)
    names=z.namelist()
    print("压缩包文件数:", len(names))
    z.extractall(dest)
    print("解压完成到 valve/")
    z.close()
except Exception as e:
    print("解压失败:", e)
PYEOF
EOF
echo "--- valve 目录文件数 ---"
find /mnt/roms/ports/Half-Life/valve -type f | wc -l

echo ""
echo "=== 检查 xash3d 能否运行 (依赖检查) ==="
ls -la /mnt/roms/ports/Half-Life/libxash.so /mnt/roms/ports/Half-Life/hl_arm64.so /mnt/roms/ports/Half-Life/client_arm64.so 2>&1

echo ""
echo "=== 检查土豆兄弟 runtime 两处 ==="
ls -la /mnt/roms/ports/PortMaster/libs/frt_3.6.squashfs /mnt/r36s/opt/system/Tools/PortMaster/libs/frt_3.6.squashfs 2>&1
'''
with sftp.open('/tmp/fix_hl.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
# 需要密码给 sudo python3
out,err=run('echo 1 | sudo -S bash /tmp/fix_hl.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
