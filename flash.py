import os, sys, time
img=r'D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.img'
disk=r'\\.\PhysicalDrive3'
if not os.path.exists(img):
    print('IMAGE NOT FOUND'); sys.exit(1)
isz=os.path.getsize(img)
print('image size: %.2f GB'%(isz/1e9), flush=True)
# quick identity check on target disk size
try:
    import ctypes
    # get disk geometry via CreateFile + DeviceIoControl not trivial; rely on earlier wmic check (94.4GB)
except Exception as e:
    print('warn:', e)
chunk=8*1024*1024
written=0
t0=time.time()
with open(img,'rb') as fi, open(disk,'r+b',buffering=0) as fo:
    while True:
        buf=fi.read(chunk)
        if not buf: break
        fo.write(buf)
        written+=len(buf)
        if written % (256*1024*1024)==0:
            el=time.time()-t0
            print('written %.2f GB, %.1f MB/s'%(written/1e9,(written/1e6)/el), flush=True)
print('FLASH DONE, total %.2f GB'%(written/1e9), flush=True)
