import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
script = r'''
#!/bin/bash
set +e
echo "=== 1. 系统 mGBA 金手指目录内容 ==="
ls -la "/mnt/r36s/home/ark/.config/retroarch/cheats/mGBA/" 2>&1
echo ""
echo "--- mGBA 里每个文件内容 ---"
for f in "/mnt/r36s/home/ark/.config/retroarch/cheats/mGBA/"*; do
  [ -f "$f" ] || continue
  echo ">>> $f"
  cat "$f"
  echo "<<<"
done

echo ""
echo "=== 2. 用户现有金手指 /mnt/roms/金手指/光明之魂2.cht ==="
cat "/mnt/roms/金手指/光明之魂2.cht" 2>&1
echo ""
echo "--- 金手指目录所有文件 ---"
ls -la /mnt/roms/金手指/ 2>&1
'''
with sftp.open('/tmp/read_cheat.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/read_cheat.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
