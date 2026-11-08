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
print('=== valve 关键文件检查 ===')
for f in ['gameinfo.txt','liblist.gam','pak0.pak','halflife.wad','dlls','cl_dlls','maps','models']:
    out,err=run(S+f'ls -la "/mnt/roms/ports/Half-Life/valve/{f}" 2>&1 | head -3')
    print(f'[{f}]:', out if out else '(不存在)')
print('\n=== 半条命 valve 总文件数 ===')
out,err=run(S+'find /mnt/roms/ports/Half-Life/valve -type f | wc -l')
print('valve 文件数:', out if out else err)
print('\n=== 检查 xash3d 依赖的库是否存在 ===')
out,err=run(S+'for f in libxash.so libxashmenu64.so client_arm64.so hl_arm64.so; do echo -n "$f: "; file /mnt/roms/ports/Half-Life/$f 2>&1 | head -1; done')
print(out if out else err)
c.close()
