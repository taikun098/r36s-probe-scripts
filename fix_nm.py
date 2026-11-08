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

print('=== 确认挂载 ===')
run(c, S+'mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s')

print('\n=== 检查无线固件 (rtl8188fu 需要什么) ===')
out,err=run(c, S+'find /mnt/r36s/lib/firmware -iname "*8188f*" 2>/dev/null')
print(out if out else err)
out,err=run(c, S+'find /mnt/r36s/lib/firmware -iname "*8188*" 2>/dev/null')
print('所有8188固件:', out if out else err)

print('\n=== 检查 ifupdown 网络接口配置 ===')
out,err=run(c, S+'cat /mnt/r36s/etc/network/interfaces 2>&1')
print(out if out else err)
out,err=run(c, S+'ls -la /mnt/r36s/etc/network/interfaces.d/ 2>&1')
print(out if out else err)

print('\n=== 修改 NetworkManager.conf: managed=true (让NM管理eth0) ===')
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/NetworkManager.conf')
print('当前:', out if out else err)
cmd=S+'''sed -i 's/managed=false/managed=true/' /mnt/r36s/etc/NetworkManager/NetworkManager.conf && echo 已改为managed=true'''
out,err=run(c, cmd)
print(out if out else err)
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/NetworkManager.conf')
print('修改后:', out if out else err)
c.close()
print('\nDONE')
