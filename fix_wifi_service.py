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
# 简化版 wifi service，去掉复杂引号/换行导致的解析错误
svc = '''[Unit]
Description=Enable old USB enumeration scheme for OTG compatibility
After=multi-user.target
DefaultDependencies=no

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo 1 > /sys/module/usbcore/parameters/old_scheme_first'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
'''
sf=c.open_sftp()
sf.putfo(io.BytesIO(svc.encode()), '/tmp/wifi.service')
out,err=run(S+'cp /tmp/wifi.service /mnt/r36s/etc/systemd/system/wifi-usb-old-scheme.service; echo cp=$?')
print(out if out else err)
print('\n=== 验证新 service 内容 ===')
out,err=run(S+'cat /mnt/r36s/etc/systemd/system/wifi-usb-old-scheme.service 2>&1')
print(out if out else err)
print('\n=== 检查依赖的 dwc2 相关配置是否引用存在 ===')
out,err=run(S+'grep -rn "wifi-usb-old-scheme" /mnt/r36s/etc/systemd/ 2>/dev/null')
print(out if out else err)
c.close()
