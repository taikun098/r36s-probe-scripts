import re

def bdecode(data, pos=0):
    def parse(p):
        c=data[p:p+1]
        if c==b'i':
            e=data.index(b'e',p); return int(data[p+1:e]), e+1
        if c==b'l':
            p+=1; lst=[]
            while data[p:p+1]!=b'e':
                v,p=parse(p); lst.append(v)
            return lst,p+1
        if c==b'd':
            p+=1; d={}
            while data[p:p+1]!=b'e':
                k,p=parse(p); v,p=parse(p); d[k]=v
            return d,p+1
        if c in b'0123456789':
            e=data.index(b':',p); n=int(data[p:e]); s=data[e+1:e+1+n]; return s,e+1+n
        raise ValueError("bad", data[p:p+20])
    return parse(pos)[0]

raw=open(r"D:\R36S_backup_20261015\darkos\dArkOS_G80CA.torrent","rb").read()
info=bdecode(raw)
out=[]
out.append("announce: %s"%info.get(b'announce'))
if b'announce-list' in info:
    out.append("announce-list:")
    for lst in info[b'announce-list']:
        out.append("   "+str([x.decode() for x in lst]))
out.append("name: %s"%info[b'info'].get(b'name'))
out.append("length: %s"%info[b'info'].get(b'length'))
open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\torrent_info.txt","w",encoding="utf-8").write("\n".join(out))
print("done")
