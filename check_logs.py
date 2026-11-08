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
print('=== 卡是否还在服务器 ===')
out,err=run(c, 'lsblk | grep -E "sdb|87.9" || echo "卡已拔出"')
print(out if out else err)
if 'sdb' in (out or ''):
    print('\n=== 挂载系统分区读日志 ===')
    run(c, S+'mkdir -p /mnt/r36s && mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s')
    out,err=run(c, S+'ls -la /mnt/r36s/var/log/ 2>&1 | head -30')
    print('日志目录:'); print(out if out else err)
    out,err=run(c, S+'ls -la /mnt/r36s/var/log/journal/ 2>&1 | head -10')
    print('journal:', out if out else err)
c.close()
print('\nDONE')
