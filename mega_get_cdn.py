import requests, json, time, os
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
url="https://g.api.mega.co.nz/cs?id=1"
data=[{'a':'g','g':1,'p':'Izo3TRzA'}]
r=requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'}, proxies=proxy, timeout=45)
j=r.json()[0]
cdn=j['g']
sz=j['s']
print("cdn:", cdn)
print("size:", sz)
# save CDN url for aria2
open(r"D:\R36S_backup_20261015\darkos\cdn_url.txt","w").write(cdn)
print("saved cdn_url.txt")
