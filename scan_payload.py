import os, zlib, zipfile, gzip, io
p=r"E:\tools\Install.PortMaster.sh"
data=open(p,'rb').read()
print("file size:",len(data))
# scan for payload signatures
# zip local header PK\x03\x04 ; gzip \x1f\x8b ; tar? 
import re
for sig,name in [ (b'PK\x03\x04','zip'), (b'\x1f\x8b\x08','gzip'), (b'\x1f\x8b','gzip2') ]:
    idx=data.find(sig)
    if idx>=0:
        print("sig",name,"at",idx,"(%.1f%% of file)"%(100*idx/len(data)))
# find makeself markers
for m in [b'_SKIPTAR', b'label=', b'UNTAR', b'tail -n', b'GZIP', b'label:' ]:
    idx=data.find(m)
    if idx>=0:
        print("marker",m,"at",idx)
# attempt: find last PK and try zip extract
pk=data.rfind(b'PK\x03\x04')
if pk>=0:
    print("last zip PK at",pk)
    try:
        zf=zipfile.ZipFile(io.BytesIO(data[pk:]))
        names=zf.namelist()
        print("zip entries:",len(names))
        for n in names[:30]:
            print("  ",n)
    except Exception as e:
        print("zip extract err:",e)
