import paramiko
def run(cli, cmd):
    i,o,e=cli.exec_command(cmd)
    out=o.read().decode('utf-8','replace').strip()
    err=e.read().decode('utf-8','replace').strip()
    return out, err
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
S='echo 1 | sudo -S '

print('=== 挂载 sdb2 (btrfs ROOTFS) 和 sdb3 (exFAT EASYROMS) ===')
for cmd in [S+'mkdir -p /mnt/r36s',
            S+'mount /dev/sdb2 /mnt/r36s 2>&1; echo M2=$?',
            S+'mkdir -p /mnt/roms',
            S+'mount /dev/sdb3 /mnt/roms 2>&1; echo M3=$?']:
    out,err=run(c, cmd)
    print(out if out else err)

print('\n=== 系统分区内容 ===')
out,err=run(c, S+'ls /mnt/r36s')
print(out if out else err)
print('\n=== NetworkManager 目录检查 ===')
out,err=run(c, S+'ls -la /mnt/r36s/etc/NetworkManager/system-connections/ 2>&1')
print(out if out else err)

print('\n=== 写入有线 DHCP 配置 ===')
conn='''[connection]
id=eth0
type=ethernet
interface-name=eth0
autoconnect=true

[ipv4]
method=auto

[ipv6]
method=auto
'''
import base64
b64=base64.b64encode(conn.encode()).decode()
cmd=S+f'echo {b64} | base64 -d | sudo tee /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection >/dev/null && sudo chmod 600 /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection && echo DHCP写入成功'
out,err=run(c, cmd)
print(out if out else err)

print('\n=== 检查游戏分区是否有无线固件 ===')
out,err=run(c, S+'ls -la /mnt/roms/ | head -25')
print(out if out else err)
out,err=run(c, S+'find /mnt/roms -maxdepth 2 -iname "*rtl8188*" 2>/dev/null')
print('固件:', out if out else '(未找到)')

print('\n=== 验证 DHCP 配置 ===')
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection')
print(out if out else err)

c.close()
print('\nDONE')
