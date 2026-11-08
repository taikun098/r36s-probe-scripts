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

print('=== 挂载状态 ===')
out,err=run(c, S+'findmnt | grep -E "sdb2|sdb3|r36s|roms"')
print(out if out else err)

print('\n=== 确保挂载 ===')
run(c, S+'mkdir -p /mnt/r36s && mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s')
run(c, S+'mkdir -p /mnt/roms && mountpoint -q /mnt/roms || mount /dev/sdb3 /mnt/roms')
out,err=run(c, S+'findmnt | grep -E "sdb2|sdb3"')
print('挂载后:', out if out else err)

print('\n=== 检查 NetworkManager 连接文件 ===')
out,err=run(c, S+'ls -la /mnt/r36s/etc/NetworkManager/system-connections/ 2>&1')
print(out if out else err)
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection 2>&1')
print('内容:', out if out else err)

print('\n=== 重新写入有线 DHCP (确保真实写入卡分区) ===')
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
cmd=S+f'echo {b64} | base64 -d | sudo tee /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection >/dev/null && sudo chmod 600 /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection && echo 写入成功'
out,err=run(c, cmd)
print(out if out else err)

print('\n=== 再次确认 ===')
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection 2>&1')
print(out if out else err)

print('\n=== 确认无线固件已存在 ===')
out,err=run(c, S+'ls -la /mnt/r36s/lib/firmware/rtlwifi/rtl8188eufw.bin')
print(out if out else err)

print('\n=== 检查无线网卡驱动模块 ===')
out,err=run(c, S+'find /mnt/r36s/lib/modules -iname "*8188*" 2>/dev/null | head')
print(out if out else err)

c.close()
print('\nDONE')
