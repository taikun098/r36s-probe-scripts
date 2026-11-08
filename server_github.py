import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
print('=== 服务器获取 Xash3D releases 信息 ===')
out,err=run('curl -sL --max-time 30 https://api.github.com/repos/FWGS/xash3d-fwgs/releases/latest 2>&1 | head -c 2000')
print(out if out else err)
print('\n=== 测试 GitHub 连通性 ===')
out,err=run('curl -sIL --max-time 20 https://github.com 2>&1 | head -5')
print(out if out else err)
c.close()
