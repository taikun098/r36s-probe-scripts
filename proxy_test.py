import requests, time
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
targets=[
 "https://www.google.com",
 "https://api.github.com",
 "https://github.com",
 "https://mega.nz",
 "https://g.api.mega.co.nz",
 "https://onedrive.live.com",
 "https://1drv.ms",
 "https://mediafire.com",
 "https://docs.google.com",
 "https://drive.google.com",
]
out=[]
for t in targets:
    try:
        r=requests.get(t, proxies=proxy, timeout=12, allow_redirects=False)
        out.append("%-32s status=%s  loc=%s"%(t, r.status_code, r.headers.get('Location','')))
    except Exception as e:
        out.append("%-32s ERR %r"%(t,e))
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\proxy_test.txt","w",encoding="utf-8").write("\n".join(out))
print("\n".join(out))
