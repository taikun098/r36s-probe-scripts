import os, sys
os.environ['http_proxy']='http://127.0.0.1:7897'
os.environ['https_proxy']='http://127.0.0.1:7897'
os.environ['HTTP_PROXY']='http://127.0.0.1:7897'
os.environ['HTTPS_PROXY']='http://127.0.0.1:7897'

from mega import Mega
mega = Mega()
m = mega.login()
url = "https://mega.nz/file/Izo3TRzA#6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
dest = r"D:\R36S_backup_20261015\darkos"
print("STARTING mega download...", file=sys.stderr, flush=True)
try:
    m.download_url(url, dest_path=dest)
    print("DONE", file=sys.stderr, flush=True)
except Exception as e:
    print("MEGA ERROR: %r" % (e,), file=sys.stderr, flush=True)
    raise
