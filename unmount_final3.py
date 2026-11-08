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
print('=== 最终验证 wifi 服务 ===')
out,err=run(S+'cat /mnt/r36s/etc/systemd/system/wifi-usb-old-scheme.service 2>&1')
print(out if out else err)
print('\n=== 卸载 ===')
out,err=run(S+'sync; sudo umount /mnt/r36s 2>&1; echo R36S=$?; sudo umount /mnt/roms 2>&1; echo ROMS=$?')
print(out if out else err)
out,err=run(S+'findmnt | grep -E "sdb2|sdb3" || echo "已全部卸载，可安全拔卡"')
print(out if out else err)
c.close()
