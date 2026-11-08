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
print('=== 解压 ===')
out,err=run(S+'mkdir -p /tmp/xash3d && tar -xzf /tmp/xash3d-arm64.tar.gz -C /tmp/xash3d 2>&1; echo T=$?')
print(out if out else err)
print('\n=== 解压结构 ===')
out,err=run(S+'find /tmp/xash3d -maxdepth 3 -type f | head -50')
print(out if out else err)
print('\n=== 顶层目录 ===')
out,err=run(S+'ls -la /tmp/xash3d/')
print(out if out else err)
c.close()
