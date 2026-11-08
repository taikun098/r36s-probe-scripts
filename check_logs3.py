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
print('=== 正确挂载 sdb2 (每个命令都加 sudo) ===')
run(c, S+'rm -rf /mnt/r36s')
run(c, S+'mkdir -p /mnt/r36s')
out,err=run(c, S+'mount /dev/sdb2 /mnt/r36s 2>&1; echo M=$?')
print(out if out else err)
print('\n=== /mnt/r36s 顶层 ===')
out,err=run(c, S+'ls /mnt/r36s')
print(out if out else err)
print('\n=== 日志目录 ===')
out,err=run(c, S+'ls -la /mnt/r36s/var/log/ 2>&1 | head -40')
print(out if out else err)
c.close()
print('\nDONE')
