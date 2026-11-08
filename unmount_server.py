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
print('=== 同步 ===')
out,err=run(c, S+'sync; echo synced')
print(out if out else err)
print('=== 卸载 sdb3 ===')
out,err=run(c, S+'umount /mnt/roms 2>&1; echo U3=$?')
print(out if out else err)
print('=== 卸载 sdb2 ===')
out,err=run(c, S+'umount /mnt/r36s 2>&1; echo U2=$?')
print(out if out else err)
print('=== 确认 ===')
out,err=run(c, S+'findmnt | grep -E "sdb2|sdb3" || echo "已全部卸载，可安全拔卡"')
print(out if out else err)
c.close()
print('DONE')
