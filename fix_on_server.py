import paramiko, time
def run(cli, cmd):
    i,o,e=cli.exec_command(cmd)
    out=o.read().decode('utf-8','replace').strip()
    err=e.read().decode('utf-8','replace').strip()
    return out, err
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
SUDO='echo 1 | sudo -S '

print('=== 测试 sudo 权限 ===')
out,err=run(c, SUDO+'true && echo sudo-ok || echo sudo-fail')
print(out, err)

print('\n=== 挂载系统分区 sdb2 和游戏分区 sdb3 ===')
for m in ['mkdir -p /mnt/r36s','mkdir -p /mnt/roms',
          'mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s',
          'mountpoint -q /mnt/roms || mount /dev/sdb3 /mnt/roms']:
    out,err=run(c, SUDO+m)
    if out: print(out)
    if err and 'already' not in err and 'password' not in err: print('  ERR:',err)

out,err=run(c, SUDO+'ls /mnt/r36s | head -20')
print('\n系统分区顶层:', out)

print('\n=== 配置有线网卡自动获取IP (DHCP) ===')
# 写 nmconnection 到系统分区
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
# 用 python 写入避免转义问题
import base64
b64=base64.b64encode(conn.encode()).decode()
cmd=SUDO+f'mkdir -p /mnt/r36s/etc/NetworkManager/system-connections && echo {b64} | base64 -d | sudo tee /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection >/dev/null && sudo chmod 600 /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection && echo DHCP配置写入成功'
out,err=run(c, cmd)
print(out, err if err else '')

print('\n=== 安装无线网卡固件 ===')
# 从游戏分区找固件
out,err=run(c, SUDO+'find /mnt/roms -maxdepth 2 -iname "*rtl8188*" 2>/dev/null')
print('游戏分区找到的固件:', out if out else '(未找到)')
# 复制固件到系统分区
cmd=SUDO+'mkdir -p /mnt/r36s/lib/firmware/rtlwifi && cp /mnt/roms/rtl8188eufw.bin /mnt/r36s/lib/firmware/rtlwifi/ 2>/dev/null && echo 无线固件安装成功 || echo 固件复制失败'
out,err=run(c, cmd)
print(out, err if err else '')

print('\n=== 验证写入结果 ===')
out,err=run(c, SUDO+'cat /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection')
print('nmconnection 内容:'); print(out)
out,err=run(c, SUDO+'ls -la /mnt/r36s/lib/firmware/rtlwifi/')
print('无线固件目录:'); print(out)

print('\n=== 卸载 ===')
out,err=run(c, SUDO+'umount /mnt/roms; umount /mnt/r36s; echo 已卸载')
print(out, err if err else '')
c.close()
print('\nDONE')
