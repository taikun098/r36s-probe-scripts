import gzip, tarfile, io, os
data=open(r"E:\tools\Install.PortMaster.sh",'rb').read()
# gzip magic positions
import re
gzs=[m.start() for m in re.finditer(rb'\x1f\x8b\x08', data)]
print("gzip positions:",gzs[:30])
# try extracting from first gzip after 27000
candidates=[g for g in gzs if g>27000]
print("candidates after 27000:",candidates[:10])
if candidates:
    off=candidates[0]
    blob=data[off:]
    try:
        raw=gzip.decompress(blob)
        print("gzip decompressed OK from",off,"->",len(raw),"bytes")
        # is it tar?
        if raw[257:262]==b'ustar':
            print("IT IS TAR")
            tf=tarfile.open(fileobj=io.BytesIO(raw))
            names=tf.getnames()
            print("tar entries:",len(names))
            for n in names[:30]: print("  ",n)
        else:
            print("first 16:",raw[:16])
    except Exception as e:
        print("gzip err:",e)
