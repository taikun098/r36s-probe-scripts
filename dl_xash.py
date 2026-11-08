import json, os, urllib.request
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
out_dir=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\hl"
os.makedirs(out_dir, exist_ok=True)

def dl(url, outname):
    try:
        r=opener.open(url, timeout=120)
        data=r.read()
        p=os.path.join(out_dir, outname)
        with open(p,'wb') as f: f.write(data)
        print(f'OK {outname}: {len(data)}B head={data[:8].hex()}')
        return len(data)
    except Exception as e:
        print(f'FAIL {url}: {type(e).__name__}')
        return 0

# 1. 获取 releases 信息
try:
    r=opener.open('https://api.github.com/repos/FWGS/xash3d-fwgs/releases/latest', timeout=60)
    info=json.load(r)
    print('最新版本:', info.get('tag_name'))
    for a in info.get('assets',[]):
        print('  asset:', a['name'], a['size'], a['browser_download_url'])
except Exception as e:
    print('releases 获取失败:', type(e).__name__)

# 2. 尝试常见 aarch64 下载路径
print('\n=== 尝试下载 aarch64 版本 ===')
dl('https://github.com/FWGS/xash3d-fwgs/releases/latest/download/xash3d-linux-aarch64', 'xash3d-linux-aarch64')
dl('https://github.com/FWGS/xash3d-fwgs/releases/download/v0.19.2/xash3d-linux-aarch64.tar.gz', 'xash3d.tar.gz')
dl('https://github.com/FWGS/xash3d-fwgs/releases/download/v0.20.1/xash3d-linux-aarch64.tar.gz', 'xash3d-v020.tar.gz')
print('DONE')
