import os, urllib.request
out_dir=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\wifi"
os.makedirs(out_dir, exist_ok=True)
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
urls=[
  'https://raw.githubusercontent.com/kelebek333/rtl8188fu/master/firmware/rtl8188fufw.bin',
  'https://raw.githubusercontent.com/lwfinger/rtl8188fu/master/firmware/rtl8188fufw.bin',
  'https://raw.githubusercontent.com/cilynx/rtl88x2bu/master/88x2bu-firmware/rtl8188fufw.bin',
]
fn=os.path.join(out_dir,'rtl8188fufw.bin')
for url in urls:
    try:
        r=opener.open(url,timeout=120)
        data=r.read()
        if len(data)<1000: 
            print(f'{url}: 太小 {len(data)},跳过'); continue
        with open(fn,'wb') as f: f.write(data)
        print(f'下载成功 {url} -> {len(data)}B head={data[:8].hex()}')
        break
    except Exception as e:
        print(f'失败 {url}: {type(e).__name__}')
print('DONE')
