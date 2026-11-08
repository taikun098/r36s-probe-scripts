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
# 在两个 ramoops 里找 Internal error Oops + 崩溃栈
for f in ['dmesg-ramoops-0','dmesg-ramoops-1','console-ramoops-0']:
    print(f'===== {f} =====')
    out,err=run(S+f'strings /mnt/r36s/var/lib/systemd/pstore/{f} 2>/dev/null | grep -n "Internal error\\|Oops\\|Call trace\\|PC is at\\|Code:" | head -20')
    print(out if out.strip() else '(无 Oops 标记)')
print('\n===== 提取 655 秒附近 Oops 崩溃栈 =====')
out,err=run(S+'strings /mnt/r36s/var/lib/systemd/pstore/dmesg-ramoops-1 2>/dev/null | grep -A 60 "Internal error: Oops" | head -70')
print(out if out else '(dmesg-ramoops-1 无)')
c.close()
