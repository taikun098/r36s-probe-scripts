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
url='https://github.com/FWGS/xash3d-fwgs/releases/download/continuous/xash3d-fwgs-linux-arm64.tar.gz'
out,err=run(f'cd /tmp && curl -sL --max-time 240 -o xash3d-arm64.tar.gz "{url}" && ls -la xash3d-arm64.tar.gz')
print(out if out else err)
out,err=run('echo 1 | sudo -S file /tmp/xash3d-arm64.tar.gz 2>/dev/null || file /tmp/xash3d-arm64.tar.gz')
print(out if out else err)
c.close()
