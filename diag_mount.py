import paramiko
def run(cli, cmd):
    i,o,e=cli.exec_command(cmd)
    out=o.read().decode('utf-8','replace').strip()
    err=e.read().decode('utf-8','replace').strip()
    return out, err
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
SUDO='echo 1 | sudo -S '

print('=== 检查 sdb2/sdb3 文件系统类型 ===')
for d in ['sdb2','sdb3']:
    out,err=run(c, SUDO+f'blkid /dev/{d}')
    print(f'{d}:', out if out else err)

print('\n=== 尝试手动挂载 sdb2 (带报错) ===')
out,err=run(c, SUDO+'mkdir -p /mnt/r36s && mount /dev/sdb2 /mnt/r36s 2>&1; echo EXIT=$?')
print(out if out else err)

print('\n=== 挂载后检查 ===')
out,err=run(c, SUDO+'ls /mnt/r36s 2>&1 | head -20')
print(out if out else err)

print('\n=== 尝试挂载 sdb3 (游戏分区) ===')
out,err=run(c, SUDO+'mkdir -p /mnt/roms && mount /dev/sdb3 /mnt/roms 2>&1; echo EXIT=$?')
print(out if out else err)
out,err=run(c, SUDO+'ls /mnt/roms 2>&1 | head -20')
print(out if out else err)

c.close()
print('\nDONE')
