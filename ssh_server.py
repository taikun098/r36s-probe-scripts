import paramiko
def run(cli, cmd):
    i,o,e=cli.exec_command(cmd)
    out=o.read().decode('utf-8','replace').strip()
    err=e.read().decode('utf-8','replace').strip()
    return out, err
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
    print('=== SSH 连接成功 (user) ===')
    cmds = ['whoami; id',
            'uname -a',
            'cat /etc/os-release 2>/dev/null | head -6',
            'hostname',
            'df -h | grep -E "Filesystem|/dev"',
            'free -h | head -2',
            'sudo -n true 2>/dev/null && echo "sudo: 免密可用" || echo "sudo: 需要密码或未配置"',
            'lsblk -o NAME,SIZE,MODEL,TRAN 2>/dev/null | head -25']
    for cmd in cmds:
        out,err = run(c, cmd)
        print('$ '+cmd)
        print(out if out else ('ERR: '+err))
        print()
    c.close()
except Exception as e:
    print('连接失败:', repr(e))
