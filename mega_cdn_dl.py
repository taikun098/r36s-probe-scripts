import requests, time, os
cdn=open(r"D:\R36S_backup_20261015\darkos\cdn_url.txt").read().strip()
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Referer':'https://mega.nz/','Accept':'*/*'}
out=r"D:\R36S_backup_20261015\darkos\dArkOS_enc.bin"
r=requests.get(cdn, headers=ua, proxies=proxy, stream=True, timeout=(30,300))
print("status", r.status_code, flush=True)
if r.status_code!=200:
    print("FAIL", r.text[:200], flush=True); raise SystemExit(1)
total=int(r.headers.get('Content-Length',0))
done=0; t0=time.time()
with open(out,'wb') as f:
    for chunk in r.iter_content(chunk_size=1<<20):
        if not chunk: continue
        f.write(chunk); done+=len(chunk)
        if done%(500<<20)==0 or done==total:
            sp=done/(time.time()-t0)/1e6
            print("  %.1f%% %d MB @%.1f MB/s"%(done/total*100,done>>20,sp),flush=True)
print("DONE", done, flush=True)
