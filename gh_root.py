import requests
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
h={'User-Agent':'Mozilla/5.0','Accept':'application/vnd.github+json'}
base="https://api.github.com/repos/southoz/dArkOS-G80CA-RE/contents/"
r=requests.get(base, proxies=proxy, timeout=30, headers=h)
print("status", r.status_code)
if r.status_code==200:
    for it in r.json():
        print(it['type'], it['name'])
else:
    print(r.text[:300])
