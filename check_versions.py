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
run(S+'mkdir -p /mnt/r36s; sudo mount /dev/sdb2 /mnt/r36s 2>&1')
print('=== dArkOS 版本信息 ===')
out,err=run(S+'cat /mnt/r36s/usr/lib/arkos/version 2>/dev/null; cat /mnt/r36s/etc/arkos-version 2>/dev/null; cat /mnt/r36s/usr/share/arkos/version 2>/dev/null; ls /mnt/r36s/opt/ 2>/dev/null')
print(out if out else '(未找到版本文件)')
print('\n=== 系统发行版信息 ===')
out,err=run(S+'cat /mnt/r36s/etc/os-release 2>/dev/null | head -8')
print(out if out else err)
print('\n=== 已装关键软件版本 ===')
cmds=[
 ('RetroArch','/mnt/r36s/usr/bin/retroarch -v 2>&1 | head -2'),
 ('mGBA','ls /mnt/r36s/usr/bin/ | grep -i mgba'),
 ('PortMaster版本','cat /mnt/roms/ports/PortMaster/version 2>/dev/null'),
 ('EmulationStation','ls /mnt/r36s/opt/ 2>/dev/null; find /mnt/r36s -maxdepth 4 -iname "*emulationstation*" -type d 2>/dev/null | head'),
]
for name,cmd in cmds:
    out,err=run(S+cmd)
    print(f'[{name}]:', out.strip() if out.strip() else err.strip())
print('\n=== apt 源配置（看是否可用）===')
out,err=run(S+'cat /mnt/r36s/etc/apt/sources.list 2>/dev/null | grep -v "^#" | head; ls /mnt/r36s/etc/apt/sources.list.d/ 2>/dev/null')
print(out if out else err)
c.close()
