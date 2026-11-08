import urllib.request, re
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
for url in ['https://portmaster.games/js/runtimes.js']:
    try:
        data=opener.open(url,timeout=60).read().decode('utf-8','ignore')
        print('len',len(data))
        # find frt 3.6 entries and any urls
        for m in set(re.findall(r'https?://[^"\'<>\s]+',data)):
            if 'frt' in m.lower() or 'squashfs' in m.lower() or 'runtime' in m.lower():
                print('URL:',m)
        # print snippets containing frt_3.6
        for m in re.finditer(r'.{80}frt_3\.6.{80}',data,re.S):
            print('---CTX---')
            print(m.group(0))
    except Exception as e:
        print('ERR',url,repr(e))
