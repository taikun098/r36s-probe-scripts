import os, sys, time
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['http_proxy']='http://127.0.0.1:7897'
from mega import Mega
mega=Mega()
print("login...", flush=True); t=time.time()
m=mega.login()
print("login %.1fs"%(time.time()-t), flush=True)
print("API g (a=g)...", flush=True); t=time.time()
try:
    fd=m._api_request({'a':'g','g':1,'p':'Izo3TRzA'})
    print("API g OK in %.1fs"%(time.time()-t), flush=True)
    print("s(size):", fd.get('s'), flush=True)
    g=fd.get('g')
    print("g(cdn):", g if isinstance(g,str) else (g[:80] if isinstance(g,list) and g else g), flush=True)
except Exception as e:
    print("API g ERR after %.1fs: %r"%(time.time()-t, e), flush=True)
