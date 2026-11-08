import requests
cdn=open(r"D:\R36S_backup_20261015\darkos\cdn_url.txt").read().strip()
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Referer':'https://mega.nz/','Accept':'*/*'}
for name, proxies in [("direct",None),("proxy",proxy)]:
    try:
        r=requests.get(cdn, headers=ua, proxies=proxies, stream=True, timeout=20)
        print(name, "status", r.status_code, "clen", r.headers.get('Content-Length'))
        if r.status_code==200:
            data=r.raw.read(64)
            print("   first64:", data[:32])
            # test a larger read
            data2=r.raw.read(1<<16)
            print("   next64KB:", len(data2))
        r.close()
    except Exception as e:
        print(name, "ERR", repr(e))
