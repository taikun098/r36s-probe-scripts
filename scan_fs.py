import struct
img=r"D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.img"
f=open(img,'rb')
import os
fsize=os.path.getsize(img)
chunk=16*1024*1024
pos=0
hsqs=[]; ext4s=[]
while pos<fsize:
    f.seek(pos); read=f.read(chunk)
    if not read: break
    # squashfs magic 'hsqs'
    i=0
    while True:
        i=read.find(b'hsqs',i)
        if i<0: break
        hsqs.append(pos+i); i+=4
    # ext4 superblock (0xEF53 at +56), scan 1024 aligned
    i=0
    while True:
        i=read.find(b'\x53\xef',i)
        if i<0: break
        # check it's superblock: block size field plausible
        if i+58<=len(read):
            bs=1024<<struct.unpack('<I',read[i+24:i+28])[0] if len(read)>=i+28 else 0
            if bs in (1024,2048,4096):
                ext4s.append(pos+i)
        i+=2
    pos+=chunk
    if len(hsqs)>10 and len(ext4s)>10: break
print("total size GB:",round(fsize/1e9,1))
print("squashfs hsqs (first 10):",hsqs[:10])
print("ext4 superblocks (first 10):",ext4s[:10])
f.close()
