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
print('=== liblist.gam ===')
out,err=run(S+'cat /mnt/roms/ports/Half-Life/valve/liblist.gam 2>&1')
print(out if out else err)
print('\n=== xash3d 文件类型/依赖 ===')
out,err=run(S+'file /mnt/roms/ports/Half-Life/xash3d 2>&1')
print(out if out else err)
print('\n=== 半条命需要的系统库是否在 R36S ===')
for lib in ['libSDL2','libGL','libopenal','libm.so','libc.so.6','libstdc++','libgcc_s','libdl','libpthread','librt','libz.so']:
    out,err=run(S+f'ls /mnt/r36s/usr/lib/aarch64-linux-gnu/ 2>/dev/null | grep -E "^{lib}"')
    if not out:
        out,err=run(S+f'find /mnt/r36s/lib /mnt/r36s/usr/lib -name "{lib}*" 2>/dev/null | head -2')
    print(f'[{lib}]:', out.strip() if out.strip() else '(缺失!)')
c.close()
