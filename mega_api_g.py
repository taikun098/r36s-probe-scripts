import os, sys, time
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['http_proxy']='http://127.0.0.1:7897'
os.environ['HTTPS_PROXY']='http://127.0.0.1:7897'
os.environ['HTTP_PROXY']='http://127.0.0.1:7897'
from mega import Mega
url = "https://mega.nz/file/Izo3TRzA#6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
path = url.split('/file/')[1].split('#')[0]
key  = url.split('#')[1]
print("file_id:", path, flush=True)
print("login...", flush=True)
t=time.time()
mega=Mega(); m=mega.login()
print("login %.1fs"%(time.time()-t), flush=True)
print("api g request...", flush=True)
t=time.time()
try:
    fd = m._api_request({'a':'g','g':1,'p':path})
    print("API g OK in %.1fs"%(time.time()-t), flush=True)
    print("response keys:", list(fd.keys()) if isinstance(fd,dict) else type(fd), flush=True)
    if isinstance(fd,dict):
        print("g keys:", list(fd.get('g',{}).keys()) if isinstance(fd.get('g'),dict) else fd.get('g'), flush=True)
except Exception as e:
    import traceback
    print("API g ERR after %.1fs: %r"%(time.time()-t, e), flush=True)
    traceback.print_exc(file=sys.stderr)
