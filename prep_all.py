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

print('=== 挂载系统分区和游戏分区 ===')
run(c, S+'mkdir -p /mnt/r36s')
run(c, S+'mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s')
run(c, S+'mkdir -p /mnt/roms')
run(c, S+'mountpoint -q /mnt/roms || mount /dev/sdb3 /mnt/roms')
out,err=run(c, S+'findmnt | grep -E "sdb2|sdb3"')
print(out if out else err)

print('\n=== 1. 写入无线固件 rtl8188fufw.bin ===')
# 先检查游戏分区有没有现成的，否则从电脑上传
out,err=run(c, S+'find /mnt/roms -maxdepth 3 -iname "rtl8188fufw*" 2>/dev/null')
print('游戏分区固件:', out if out else '(无，将上传)')

print('\n=== 2. 查看移植游戏目录与日志 ===')
out,err=run(c, S+'ls /mnt/roms/ports/ 2>&1')
print('ports目录:'); print(out if out else err)
out,err=run(c, S+'for d in /mnt/roms/ports/*/log.txt; do echo "--- $d ---"; cat "$d" 2>/dev/null | tail -15; done')
print(out if out else err)

c.close()
print('\nDONE-准备阶段')
