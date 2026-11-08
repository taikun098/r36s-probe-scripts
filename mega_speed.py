import requests, time, os
cdn=open(r"D:\R36S_backup_20261015\darkos\cdn_url.txt").read().strip()
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Referer':'https://mega.nz/','Accept':'*/*'}
r=requests.get(cdn, headers=ua, proxies=proxy, stream=True, timeout=(30,300))
print("status", r.status_code, flush=True)
if r.status_code!=200:
    print("FAIL", flush=True); raise SystemExit(1)
out=open(r"D:\R36S_backup_20261015\darkos\speed_test.bin","wb")
t0=time.time(); n=0
while time.time()-t0<30:
    b=r.raw.read(1<<20)
    if not b: break
    out.write(b); n+=len(b)
out.close()
dur=time.time()-t0
print("30s downloaded: %d MB  speed: %.2f MB/s"%(n>>20, n/dur/1e6), flush=True)
