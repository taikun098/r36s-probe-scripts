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
print('=== 内核 USB 网卡驱动目录 ===')
out,err=run(S+'ls /mnt/r36s/lib/modules/4.4.189/kernel/drivers/net/usb/ 2>&1')
print(out if out else err)
print('\n=== 所有网卡驱动模块 (net) ===')
out,err=run(S+'find /mnt/r36s/lib/modules/4.4.189/kernel/drivers/net -iname "*.ko" 2>/dev/null | head -40')
print(out if out else err)
print('\n=== 检查 dm9601 固件需求 ===')
out,err=run(S+'find /mnt/r36s/lib/firmware -iname "*dm96*" -o -iname "*cdc*" 2>/dev/null')
print(out if out else err)
c.close()
