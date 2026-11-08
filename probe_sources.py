import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
# 测试服务器能否访问多个源
urls = {
 'github-releases-api':'https://api.github.com/repos/FWGS/xash3d-fwgs/tags',
 'github-release-list':'https://api.github.com/repos/FWGS/xash3d-fwgs/releases',
 'gitee-xash':'https://gitee.com/explore/all',
 'github-raw':'https://raw.githubusercontent.com/FWGS/xash3d-fwgs/master/README.md',
}
for name,u in urls.items():
    out,err=run(f'curl -sIL --max-time 15 "{u}" 2>&1 | head -3')
    print(f'[{name}]', out.strip() if out.strip() else f'(无响应/失败) {err.strip()[:50]}')
c.close()
