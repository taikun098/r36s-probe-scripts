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
print('=== 挂载游戏分区 sdb3 ===')
run(S+'mkdir -p /mnt/roms; sudo mount /dev/sdb3 /mnt/roms 2>&1')
out,err=run(S+'ls /mnt/roms/ports/ 2>&1')
print('ports:', out if out else err)

print('\n=== 半条命目录 ===')
out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/ 2>&1')
print(out if out else err)
print('\n=== 半条命启动脚本 ===')
out,err=run(S+'cat /mnt/roms/ports/Half-Life.sh 2>&1')
print(out if out else err)
print('\n=== xash3d 大小 ===')
out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/xash3d /mnt/roms/ports/Half-Life/libxash.so /mnt/roms/ports/Half-Life/hl_arm64.so 2>&1')
print(out if out else err)

print('\n=== WiFi 服务配置 ===')
out,err=run(S+'find /mnt/r36s/etc/systemd/system -iname "*wifi*" 2>/dev/null; echo ---; cat /mnt/r36s/etc/systemd/system/wifi-usb-old-scheme.service 2>&1')
print(out if out else err)
print('\n=== WiFi 相关服务全部 ===')
out,err=run(S+'ls /mnt/r36s/etc/systemd/system/*.service 2>/dev/null | head; echo ---; find /mnt/r36s -name "wifi-usb-old-scheme.service" 2>/dev/null')
print(out if out else err)
c.close()
