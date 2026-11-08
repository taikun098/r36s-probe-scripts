import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()

# 用户的金手指数据
cheats = [
    ("无限HP", "03003E4C:03E7"),
    ("无限MP", "03003E4A:2706"),
    ("魂槽满必杀无限", "03003E4E:00FF"),
    ("能力点999", "02003C12:03E7"),
    ("技能点999", "02003C28:03E7"),
    ("经验超多快速升级", "02003C14:3B9AC9FF"),
    ("背包第1格=钱袋", "02003D48:0A"),
    ("金钱65535", "02003D4A:FFFF"),
    ("背包第1格 秘银矿石", "02003D48:0904"),
    ("背包第1格 黑暗矿石", "02003D48:0903"),
    ("背包第1格 光辉矿石", "02003D48:0902"),
    ("背包第1格 魂之装备", "02003D48:0700"),
    ("背包第1格 复活羽毛", "02003D48:010B"),
    ("背包第1格 万能药", "02003D48:0107"),
    ("背包第1格 大回复药", "02003D48:0103"),
    ("技能集气超快", "03003DAC:0007"),
    ("敌人一击秒杀", "03003E54:0001"),
]

# 生成 mGBA 格式
lines=[]
for i,(name,code) in enumerate(cheats):
    lines.append(f'cheat{i}_desc = "{name}"')
    lines.append(f'cheat{i}_code = "{code}"')
    lines.append(f'cheat{i}_enable = "false"')
    lines.append('')
lines.append(f'cheats = "{len(cheats)}"')
content = '\n'.join(lines) + '\n'

# 上传并写入
script = f'''#!/bin/bash
set +e
echo "=== 写入新格式金手指 ==="
cat > "/mnt/roms/金手指/光明之魂2.cht" <<'CHEOF'
{content}
CHEOF
echo "--- 写入结果 ---"
cat "/mnt/roms/金手指/光明之魂2.cht"
echo ""
echo "--- 文件信息 ---"
ls -la "/mnt/roms/金手指/光明之魂2.cht"
'''
with sftp.open('/tmp/write_cheat.sh','w') as f:
    f.write(script)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
out,err=run('echo 1 | sudo -S bash /tmp/write_cheat.sh')
print(out)
if err and 'password' not in err: print('ERR:',err)
c.close()
