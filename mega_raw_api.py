import requests, json, time
proxy={'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'}
url="https://g.api.mega.co.nz/cs?id=1"
data=[{'a':'g','g':1,'p':'Izo3TRzA'}]
t=time.time()
try:
    r=requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'}, proxies=proxy, timeout=45)
    print("status",r.status_code,"in %.1fs"%(time.time()-t))
    print("resp[:800]:", r.text[:800])
except Exception as e:
    print("ERR after %.1fs: %r"%(time.time()-t,e))
