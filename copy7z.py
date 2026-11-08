import shutil, os, time
src=r"D:\R36S_backup_20261015\darkos\dArkOS_G80CA-RE_trixie_02062026.7z"
dst=r"D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.7z"
f=open(src,'rb'); print("head", f.read(8).hex(), flush=True); f.close()
t0=time.time()
shutil.copyfile(src,dst)
print("copied in %.0fs"%(time.time()-t0), flush=True)
print("size", os.path.getsize(dst), flush=True)
