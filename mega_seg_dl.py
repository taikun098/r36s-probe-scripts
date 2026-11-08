import requests, json, time, os, sys
total=3719990947
out=r"D:\R36S_backup_20261015\darkos\dArkOS_enc.bin"
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Referer':'https://mega.nz/','Accept':'*/*'}
offset = os.path.getsize(out) if os.path.exists(out) else 0
SEG=256<<20
t0=time.time()
fail=0
def new_cdn():
    r=requests.post("https://g.api.mega.co.nz/cs?id=1", data=json.dumps([{'a':'g','g':1,'p':'Izo3TRzA'}]), headers={'Content-Type':'application/json'}, proxies=proxy, timeout=45)
    return r.json()[0]['g']
while offset<total:
    try:
        cdn=new_cdn()
        end=min(offset+SEG-1,total-1)
        h=dict(ua); h['Range']='bytes=%d-%d'%(offset,end)
        rr=requests.get(cdn, headers=h, proxies=proxy, stream=True, timeout=(30,300))
        if rr.status_code not in (200,206):
            print("offset %d status %d, retry"%(offset,rr.status_code),flush=True)
            fail+=1
            if fail>12: print("too many fails, abort",flush=True); break
            time.sleep(2); continue
        fail=0
        wrote=0
        with open(out,'ab') as f:
            for chunk in rr.iter_content(1<<20):
                if not chunk: break
                f.write(chunk); wrote+=len(chunk)
        offset+=wrote
        sp=offset/(time.time()-t0)/1e6
        print("offset %d (%.1f%%) %.0f MB  sp %.2f MB/s"%(offset,offset/total*100,offset>>20,sp),flush=True)
        rr.close()
    except Exception as e:
        print("ERR %r"%(e,),flush=True); fail+=1
        if fail>12: print("too many fails, abort",flush=True); break
        time.sleep(2)
print("DONE",offset,flush=True)
