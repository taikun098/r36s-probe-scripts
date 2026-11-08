import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
print("=== USB 设备 (网卡) ===")
out,err=run('lsusb')
print(out if out else err)
print("\n=== 网络接口 ===")
out,err=run('ip -br link')
print(out if out else err)
print("\n=== TF卡是否插着 ===")
out,err=run('lsblk | grep -E "sdb|87.9"')
print(out if out else err)
c.close()
