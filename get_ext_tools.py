import urllib.request, re, json
proxy=urllib.request.ProxyHandler({'http':'http://127.0.0.1:7897','https':'http://127.0.0.1:7897'})
opener=urllib.request.build_opener(proxy)
opener.addheaders=[('User-Agent','Mozilla/5.0')]

def get(url,timeout=60):
    return opener.open(url,timeout=timeout).read().decode('utf-8','ignore')

print('=== DiskInternals Linux Reader ===')
try:
    html=get('https://www.diskinternals.com/linux-reader/')
    exes=set(re.findall(r'href="([^"]*\.exe[^"]*)"',html,re.I))
    print('exe links:',exes)
    for m in set(re.findall(r'https?://[^"\'<>\s]+',html)):
        if 'download' in m.lower() or '.exe' in m.lower():
            print('URL:',m)
except Exception as e:
    print('ERR',repr(e))

print()
print('=== Ext4Fsd GitHub releases ===')
try:
    d=json.loads(get('https://api.github.com/repos/bobranten/Ext4Fsd/releases/latest'))
    print('release:',d.get('tag_name'))
    for a in d.get('assets',[]):
        print('ASSET:',a['name'],'| %.1fMB'%(a['size']/1048576),'|',a['browser_download_url'])
except Exception as e:
    print('ERR',repr(e))
