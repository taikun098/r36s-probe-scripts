import os, sys, json, time
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['http_proxy']='http://127.0.0.1:7897'
from mega import Mega
import requests
mega=Mega()
print("login...", flush=True); t=time.time()
m=mega.login()
print("login %.1fs"%(time.time()-t), flush=True)
url = "https://mega.nz/file/Izo3TRzA#6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
file_id = url.split('/file/')[1].split('#')[0]
print("api_url:", m.api_url, flush=True)
print("has sid:", bool(getattr(m,'sid',None)), flush=True)
# build API g request manually with timeout
seq = m.sequence_num()
api_url = m.api_url + "?id=" + str(seq)
if getattr(m,'sid',None):
    api_url += "&sid=" + m.sid
data=[{'a':'g','g':1,'p':file_id}]
proxies={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
print("POST API g (timeout 30)...", flush=True); t=time.time()
try:
    r=requests.post(api_url, data=json.dumps(data), headers={'Content-Type':'application/json'}, timeout=30, proxies=proxies)
    print("status", r.status_code, "in %.1fs"%(time.time()-t), flush=True)
    print("resp[:600]:", r.text[:600], flush=True)
except Exception as e:
    print("API g ERR after %.1fs: %r"%(time.time()-t, e), flush=True)
