import paramiko, io
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
S='echo 1 | sudo -S '
# 上传 wifi.conf
sf=c.open_sftp()
sf.putfo(io.BytesIO(b'r8188eu\n'), '/tmp/wifi.conf')
print('wifi.conf 已上传')

out,err=run(S+'mkdir -p /mnt/r36s/etc/modules-load.d; cp /tmp/wifi.conf /mnt/r36s/etc/modules-load.d/wifi.conf; echo 已写入; cat /mnt/r36s/etc/modules-load.d/wifi.conf')
print(out if out else err)

print('\n=== r8188eu.ko 信息 ===')
out,err=run(S+'cat /mnt/r36s/lib/modules/4.4.189/modules.dep 2>/dev/null | grep r8188eu')
print(out if out else '(无依赖记录)')
out,err=run(S+'ls -la /mnt/r36s/lib/modules/4.4.189/kernel/drivers/staging/rtl8188eu/r8188eu.ko')
print(out if out else err)
c.close()
