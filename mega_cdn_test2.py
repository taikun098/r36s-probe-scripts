import requests, json, time
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
# 1. fresh CDN
r=requests.post("https://g.api.mega.co.nz/cs?id=1", data=json.dumps([{'a':'g','g':1,'p':'Izo3TRzA'}]), headers={'Content-Type':'application/json'}, proxies=proxy, timeout=45)
cdn=r.json()[0]['g']
print("fresh cdn:", cdn[:50], flush=True)
open(r"D:\R36S_backup_20261015\darkos\cdn_url.txt","w").write(cdn)
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Referer':'https://mega.nz/','Accept':'*/*'}
# 2. direct + proxy test
for name,proxies in [("direct",None),("proxy",proxy)]:
    try:
        rr=requests.get(cdn, headers=ua, proxies=proxies, stream=True, timeout=20)
        print(name, "status", rr.status_code, "clen", rr.headers.get('Content-Length'), flush=True)
        if rr.status_code==200:
            print("  got", len(rr.raw.read(2048)), "bytes", flush=True)
        rr.close()
    except Exception as e:
        print(name,"ERR",repr(e), flush=True)
