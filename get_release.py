import urllib.request, json
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
try:
    d=json.loads(opener.open('https://api.github.com/repos/PortsMaster/PortMaster-Runtime/releases/latest',timeout=60).read().decode('utf-8'))
    print('release:',d.get('tag_name'))
    for a in d.get('assets',[]):
        n=a['name']
        if 'frt' in n.lower() or 'squashfs' in n.lower() or '3.6' in n:
            print('ASSET:',n,'| %.1fMB'%(a['size']/1048576),'|',a['browser_download_url'])
except Exception as e:
    print('ERR',repr(e))
