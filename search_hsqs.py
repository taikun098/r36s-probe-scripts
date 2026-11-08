import os, sys
f=r'D:\R36S_backup_20261015\extract\rootfs\1.img'
size=os.path.getsize(f)
out=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\rootfs_probe.txt"
res=["size=%d"%size]
with open(f,'rb') as fp:
    off=0
    chunk=b''
    carry=b''
    while True:
        blk=fp.read(1<<20)
        if not blk: break
        data=carry+blk
        for m in [b'hsqs',b'\\xed\\x26\\x01\\x53']:
            i=data.find(m)
            if i>=0:
                res.append("%s at abs offset %d"%(m, off+ i - len(carry)))
        carry=data[-4:]
        off+=len(blk)
        if off % (8<<20)==0:
            sys.stderr.write("scanned %d MB\n"% (off>>20))
# also read gzip header region
with open(f,'rb') as fp:
    fp.seek(6426009)
    res.append("gzip region @6426009: "+fp.read(32).hex())
open(out,'w').write("\n".join(res))
print("done, %d hits"%(len(res)-2))
