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
print('=== valve/dlls 内容 ===')
out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/valve/dlls/ 2>&1')
print(out if out else err)
print('\n=== valve/cl_dlls 内容 ===')
out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/valve/cl_dlls/ 2>&1')
print(out if out else err)
print('\n=== 移植包自带的 ARM 库 ===')
out,err=run(S+'ls -la /mnt/roms/ports/Half-Life/*arm64.so 2>&1')
print(out if out else err)
c.close()
