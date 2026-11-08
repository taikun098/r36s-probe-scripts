import os, sys, time
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['http_proxy']='http://127.0.0.1:7897'
import requests
_orig_get = requests.get
_orig_post = requests.post
PROXIES={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
def get_wp(url, **kw):
    kw.setdefault('timeout',(10,600))
    kw.setdefault('proxies',PROXIES)
    return _orig_get(url, **kw)
def post_wp(url, **kw):
    kw.setdefault('timeout',(10,600))
    kw.setdefault('proxies',PROXIES)
    return _orig_post(url, **kw)
requests.get = get_wp
requests.post = post_wp
from mega import Mega
mega=Mega()
print("login...", flush=True); t=time.time()
m=mega.login()
print("login %.1fs"%(time.time()-t), flush=True)
link="https://mega.nz/file/Izo3TRzA#6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
print("downloading...", flush=True); t=time.time()
try:
    m.download_url(link, dest_path=r"D:\R36S_backup_20261015\darkos")
    print("DONE in %.1fs"%(time.time()-t), flush=True)
except Exception as e:
    print("DL ERR after %.1fs: %r"%(time.time()-t, e), flush=True)
