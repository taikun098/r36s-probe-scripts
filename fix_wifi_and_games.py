import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()

# 上传固件
sftp.put(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\wifi\rtl8188fufw.bin", "/tmp/rtl8188fufw.bin")
print("固件已上传到服务器 /tmp/rtl8188fufw.bin")

# 写服务器脚本
script = r'''
#!/bin/bash
set +e
echo "=== 挂载分区 ==="
mkdir -p /mnt/r36s
mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s
mkdir -p /mnt/roms
mountpoint -q /mnt/roms || mount /dev/sdb3 /mnt/roms
echo "挂载状态:"; findmnt | grep -E "sdb2|sdb3"

echo ""
echo "=== 1. 写入无线固件 ==="
mkdir -p /mnt/r36s/lib/firmware/rtlwifi
cp /tmp/rtl8188fufw.bin /mnt/r36s/lib/firmware/rtlwifi/rtl8188fufw.bin
ls -la /mnt/r36s/lib/firmware/rtlwifi/rtl8188fufw.bin
echo "固件已写入"

echo ""
echo "=== 2. 配置开机自动连接 WiFi JiaYuan ==="
mkdir -p /mnt/r36s/etc/NetworkManager/system-connections
cat > /mnt/r36s/etc/NetworkManager/system-connections/JiaYuan.nmconnection <<'EOF2'
[connection]
id=JiaYuan
type=wifi
interface-name=wlan0
autoconnect=true

[wifi]
ssid=JiaYuan
mode=infrastructure

[wifi-security]
key-mgmt=wpa-psk
psk=13314832527.

[ipv4]
method=auto

[ipv6]
method=auto
EOF2
chmod 600 /mnt/r36s/etc/NetworkManager/system-connections/JiaYuan.nmconnection
echo "WiFi 配置已写入:"
cat /mnt/r36s/etc/NetworkManager/system-connections/JiaYuan.nmconnection

echo ""
echo "=== 3. 查看移植游戏日志 ==="
echo "--- ports 目录列表 ---"
ls /mnt/roms/ports/ 2>&1
echo ""
echo "--- 各游戏日志 ---"
for d in /mnt/roms/ports/*/; do
  nm=$(basename "$d")
  echo "=== [$nm] ==="
  if [ -f "${d}log.txt" ]; then
    tail -20 "${d}log.txt"
  else
    echo "(无 log.txt)"
  fi
  echo ""
done
'''
with sftp.open('/tmp/fix_all.sh','w') as f:
    f.write(script)
print("脚本已上传")

# 执行
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/fix_all.sh')
print("=== 输出 ===")
print(out)
if err and 'password' not in err:
    print("ERR:", err)
c.close()
