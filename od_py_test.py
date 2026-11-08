import sys
try:
    import requests
    print("requests OK", flush=True)
except Exception as e:
    print("requests missing:", e, flush=True); sys.exit(1)
proxies={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
url="https://1drv.ms/u/c/ea159b785597670e/IQCFDwCK7Wh2T7hEvkeGW5uuAdHxmH6WWn35SJEKEc3xsfU?e=HORFat&download=1"
print("HEAD onedrive via python...", flush=True)
try:
    r=requests.head(url, proxies=proxies, timeout=40, allow_redirects=True, verify=False)
    print("status", r.status_code, flush=True)
    print("len", r.headers.get('Content-Length'), flush=True)
    print("type", r.headers.get('Content-Type'), flush=True)
    print("final", r.url, flush=True)
except Exception as e:
    print("ERR", repr(e), flush=True)
