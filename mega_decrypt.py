import base64, sys, os, time
from Crypto.Cipher import AES
from Crypto.Util import Counter

key_b64 = "6CAO5SIFsOxxPBbdwWZV6NvjHn5NJcur0XuVX_-fA3g"
key_b64 += "=" * ((4 - len(key_b64) % 4) % 4)
kb = base64.urlsafe_b64decode(key_b64)
fk = [int.from_bytes(kb[i*4:(i+1)*4],'big') for i in range(8)]
k = (fk[0]^fk[4], fk[1]^fk[5], fk[2]^fk[6], fk[3]^fk[7])
iv = fk[4:6] + [0,0]
k_str = b''.join(x.to_bytes(4,'big') for x in k)
ctr = Counter.new(128, initial_value=((iv[0]<<32)+iv[1])<<64)
aes = AES.new(k_str, AES.MODE_CTR, counter=ctr)

src = r"D:\R36S_backup_20261015\darkos\dArkOS_enc.bin"
dst = r"D:\R36S_backup_20261015\darkos\dArkOS_G80CA-RE_trixie_02062026.7z"
sz = os.path.getsize(src)
print("source %d bytes" % sz, flush=True)
t0=time.time(); done=0
with open(src,'rb') as fi, open(dst,'wb') as fo:
    while True:
        b = fi.read(1<<20)
        if not b: break
        fo.write(aes.decrypt(b))
        done += len(b)
        if done % (200<<20) == 0:
            print("  %.1f%% %.0fs"%(done/sz*100, time.time()-t0), flush=True)
print("DECRYPTED to %s" % dst, flush=True)
print("dst size:", os.path.getsize(dst), flush=True)
