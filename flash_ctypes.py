import ctypes, os, time, sys
k=ctypes.windll.kernel32
GENERIC_WRITE=0x40000000
FILE_SHARE_READ=0x1; FILE_SHARE_WRITE=0x2
OPEN_EXISTING=3
path=r'\\.\PhysicalDrive3'
h=k.CreateFileW(path, GENERIC_WRITE, FILE_SHARE_READ|FILE_SHARE_WRITE, None, OPEN_EXISTING, 0, None)
if h==-1 or h==0:
    print('CreateFile FAILED err', k.GetLastError()); sys.exit(1)
print('opened PhysicalDrive3 OK, handle', h, flush=True)
img=r'D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.img'
isz=os.path.getsize(img)
print('image %.2f GB'%(isz/1e9), flush=True)
chunk=4*1024*1024
written=0
t0=time.time()
try:
    with open(img,'rb') as fi:
        while True:
            buf=fi.read(chunk)
            if not buf: break
            wrote=ctypes.c_ulong(0)
            ok=k.WriteFile(h, buf, len(buf), ctypes.byref(wrote), None)
            if not ok:
                print('WriteFile FAILED err', k.GetLastError(), 'at GB', round(written/1e9,2), flush=True)
                break
            written+=wrote.value
            if written%(256<<20)==0:
                el=time.time()-t0
                print('written %.2f GB, %.0f MB/s'%(written/1e9,(written/1e6)/el), flush=True)
finally:
    k.CloseHandle(h)
print('DONE total %.2f GB in %.1f min'%(written/1e9,(time.time()-t0)/60), flush=True)
