import os, sys, time
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['http_proxy']='http://127.0.0.1:7897'
os.environ['HTTPS_PROXY']='http://127.0.0.1:7897'
os.environ['HTTP_PROXY']='http://127.0.0.1:7897'
from mega import Mega
print("calling login...", flush=True)
t=time.time()
try:
    mega=Mega()
    m=mega.login()
    print("login done in %.1fs"%(time.time()-t), flush=True)
    url="https://mega.nz/file/Izo3TRzA#6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
    print("getting url info...", flush=True)
    t=time.time()
    info=m.get_public_url_info(url)
    print("info:", info, "in %.1fs"%(time.time()-t), flush=True)
except Exception as e:
    import traceback
    print("ERR:", repr(e), flush=True)
    traceback.print_exc(file=sys.stderr)
