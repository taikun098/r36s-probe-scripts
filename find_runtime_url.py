import urllib.request, re, sys
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
try:
    html=opener.open('https://portmaster.games/runtimes.html',timeout=60).read().decode('utf-8','ignore')
    print('html len',len(html))
    # find all urls containing frt or squashfs
    urls=set()
    for m in re.findall(r'https?://[^"\'<>\s]+',html):
        if 'frt' in m.lower() or 'squashfs' in m.lower() or 'runtime' in m.lower():
            urls.add(m)
    print('--- urls found:',len(urls))
    for u in sorted(urls): print(u)
except Exception as e:
    print('ERR',repr(e))
