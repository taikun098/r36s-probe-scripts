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
print('=== 验证写入 ===')
out,err=run(S+'cat /mnt/r36s/etc/modules-load.d/wifi.conf 2>&1')
print('wifi.conf:', out if out else err)
out,err=run(S+'ls /mnt/r36s/etc/NetworkManager/system-connections/ 2>&1')
print('NM连接:', out if out else err)
print('\n=== 卸载 ===')
out,err=run(S+'sync; sudo umount /mnt/r36s 2>&1; echo U=$?')
print(out if out else err)
out,err=run(S+'findmnt | grep sdb2 || echo "已卸载，可安全拔卡"')
print(out if out else err)
c.close()
