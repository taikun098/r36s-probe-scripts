import requests
u='https://1drv.ms/u/c/ea159b785597670e/IQCFDwCK7Wh2T7hEvkeGW5uuAdHxmH6WWn35SJEKEc3xsfU?e=HORFat'
proxies={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
try:
    r=requests.head(u, proxies=proxies, timeout=30, allow_redirects=True, verify=False)
    print("status", r.status_code)
    print("len", r.headers.get('Content-Length'))
    print("type", r.headers.get('Content-Type'))
    print("final", r.url)
    print("disp", r.headers.get('Content-Disposition'))
except Exception as e:
    print("ERR", repr(e))
