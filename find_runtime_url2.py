import urllib.request, re
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
try:
    html=opener.open('https://portmaster.games/runtimes.html',timeout=60).read().decode('utf-8','ignore')
    # print scripts/data refs and any .json/.js
    for m in re.findall(r'(?:src|href|data-url)="([^"]+)"',html):
        print('REF:',m)
    print('--- any github/api/aws urls ---')
    for m in set(re.findall(r'https?://[^"\'<>\s]+',html)):
        print('URL:',m)
except Exception as e:
    print('ERR',repr(e))
