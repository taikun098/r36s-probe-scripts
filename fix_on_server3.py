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

print('=== 重新挂载 (可能已挂载) ===')
run(c, S+'mkdir -p /mnt/r36s')
run(c, S+'mountpoint -q /mnt/r36s || mount /dev/sdb2 /mnt/r36s')
run(c, S+'mkdir -p /mnt/roms')
run(c, S+'mountpoint -q /mnt/roms || mount /dev/sdb3 /mnt/roms')

print('=== 安装无线网卡固件 ===')
out,err=run(c, S+'mkdir -p /mnt/r36s/lib/firmware/rtlwifi && cp /mnt/roms/rtl8188eufw.bin /mnt/r36s/lib/firmware/rtlwifi/rtl8188eufw.bin && echo 固件复制成功')
print(out if out else err)

print('\n=== 验证固件 ===')
out,err=run(c, S+'ls -la /mnt/r36s/lib/firmware/rtlwifi/')
print(out if out else err)

print('\n=== 验证完整结果 ===')
out,err=run(c, S+'echo "--- 有线DHCP配置 ---" && cat /mnt/r36s/etc/NetworkManager/system-connections/eth0.nmconnection')
print(out if out else err)
out,err=run(c, S+'echo "--- /roms 链接检查 ---" && ls -la /mnt/r36s/roms 2>&1')
print(out if out else err)

print('\n=== 卸载 ===')
out,err=run(c, S+'sync && umount /mnt/roms && umount /mnt/r36s && echo 已安全卸载')
print(out if out else err)

c.close()
print('\nDONE - 全部完成')
