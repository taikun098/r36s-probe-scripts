import requests, json
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
h={'User-Agent':'Mozilla/5.0','Accept':'application/vnd.github+json'}
r=requests.get("https://raw.githubusercontent.com/southoz/dArkOSRE-R36/main/files/BOOT/boot.ini", proxies=proxy, timeout=30, headers=h)
print("boot.ini status", r.status_code)
print("====boot.ini=====")
print(r.text)
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\gh_boot.ini.txt","w",encoding='utf-8').write(r.text)
r2=requests.get("https://api.github.com/repos/southoz/dArkOSRE-R36/contents/files/BOOT/dtb/clone/G80C-MB%20V1.1-20250319%20Panel%208", proxies=proxy, timeout=30, headers=h)
print("panel8 status", r2.status_code)
for it in r2.json():
    print(it['type'], it['name'], it.get('size'))
