import paramiko
def run(cli, cmd):
    i,o,e=cli.exec_command(cmd)
    out=o.read().decode('utf-8','replace').strip()
    err=e.read().decode('utf-8','replace').strip()
    return out, err
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
S='echo 1 | sudo -S '
print('=== NetworkManager.conf ===')
out,err=run(c, S+'cat /mnt/r36s/etc/NetworkManager/NetworkManager.conf')
print(out if out else err)
print('\n=== NetworkManager.state ===')
out,err=run(c, S+'cat /mnt/r36s/var/lib/NetworkManager/NetworkManager.state')
print(out if out else err)
print('\n=== dmesg-ramoops-0 (内核崩溃记录) ===')
out,err=run(c, S+'strings /mnt/r36s/var/lib/systemd/pstore/dmesg-ramoops-0 2>/dev/null | grep -iE "panic|error|fail|wifi|rtl|8188|eth|dhcp|fatal|BUG|Oops" | head -30')
print(out if out else '(无匹配或空)')
print('\n=== dmesg-ramoops-0 尾部 ===')
out,err=run(c, S+'strings /mnt/r36s/var/lib/systemd/pstore/dmesg-ramoops-0 2>/dev/null | tail -40')
print(out if out else '(空)')
c.close()
print('\nDONE')
