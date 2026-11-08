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
print('=== 挂载 ===')
run(S+'mkdir -p /mnt/r36s; sudo mount /dev/sdb2 /mnt/r36s 2>&1')
print('mounted')
print('\n=== 找到 pstore/ramoops 文件 ===')
out,err=run(S+'ls -la /mnt/r36s/var/lib/systemd/pstore/ 2>&1')
print(out if out else err)
print('\n=== 提取 Oops 完整崩溃栈 ===')
# 读 dmesg-ramoops，提取 Oops 到文件末尾的 Call trace
out,err=run(S+'strings /mnt/r36s/var/lib/systemd/pstore/dmesg-ramoops-0 2>/dev/null | awk \'BEGIN{p=0} /Oops/{p=1} p{print} /---\[ end/{exit}\' | head -80')
print(out if out else err)
c.close()
