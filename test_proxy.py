import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
print('=== 测试代理 192.168.0.6:7897 ===')
out,err=run('curl -sIL --max-time 15 -x http://192.168.0.6:7897 https://github.com 2>&1 | head -5')
print(out if out else f'(失败) {err[:100]}')
out,err=run('curl -sL --max-time 30 -x http://192.168.0.6:7897 "https://api.github.com/repos/FWGS/xash3d-fwgs/releases/tags/continuous" 2>&1 | head -c 300')
print('代理API测试:', out if out else err[:100])
c.close()
