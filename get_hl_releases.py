import paramiko
c=paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('192.168.0.30', username='user', password='******', timeout=10, allow_agent=False, look_for_keys=False)
def run(cmd):
    i,o,e=c.exec_command(cmd)
    out=o.read().decode('utf-8','replace')
    err=e.read().decode('utf-8','replace')
    return out, err
print('=== 获取 xash3d-fwgs releases 列表 ===')
out,err=run('curl -sL --max-time 30 https://api.github.com/repos/FWGS/xash3d-fwgs/releases 2>&1')
if not out:
    print('无输出:', err[:200])
else:
    # 提取 release tag + assets
    import json
    try:
        rels=json.loads(out)
        print(f'共 {len(rels)} 个 release')
        for r in rels[:3]:
            print('\n[', r.get('tag_name'), ']', r.get('name'))
            for a in r.get('assets',[]):
                print('   asset:', a['name'], a['size'])
    except Exception as e:
        print('解析失败:', e, out[:300])
c.close()
