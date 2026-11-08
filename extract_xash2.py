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
out,err=run(S+'rm -rf /tmp/xash3d && mkdir -p /tmp/xash3d && chmod 777 /tmp/xash3d && tar -xzf /tmp/xash3d-arm64.tar.gz -C /tmp/xash3d 2>&1; echo T=$?')
print(out if out else err)
print('\n=== 解压顶层 ===')
out,err=run(S+'ls -la /tmp/xash3d/xash3d-fwgs-linux-arm64/ 2>&1')
print(out if out else err)
print('\n=== 关键文件大小 ===')
out,err=run(S+'ls -la /tmp/xash3d/xash3d-fwgs-linux-arm64/xash3d /tmp/xash3d/xash3d-fwgs-linux-arm64/libxash.so 2>&1')
print(out if out else err)
c.close()
