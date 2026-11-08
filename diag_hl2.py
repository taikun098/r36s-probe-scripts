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
print('=== 卡是否在服务器 ===')
out,err=run('lsblk | grep -E "sdb|87.9"')
print(out if out else '卡不在服务器')
if 'sdb' in (out or ''):
    run(S+'mkdir -p /mnt/r36s; sudo mount /dev/sdb2 /mnt/r36s 2>/dev/null')
    print('\n=== 系统日志错误检查 (ramoops) ===')
    out,err=run(S+'strings /mnt/r36s/var/lib/systemd/pstore/dmesg-ramoops-0 2>/dev/null | grep -iE "panic|Oops|BUG|fatal|error" | head -20')
    print(out if out else '(无新错误)')
    print('\n=== 半条命目录详细 ===')
    out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/ 2>&1')
    print(out if out else err)
    print('\n=== 半条命启动脚本 ===')
    out,err=run(S+'cat /mnt/roms/ports/Half-Life.sh 2>&1')
    print(out if out else err)
    print('\n=== xash3d 文件大小/依赖 ===')
    out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/xash3d /mnt/roms/ports/Half-Life/libxash.so 2>&1')
    print(out if out else err)
c.close()
