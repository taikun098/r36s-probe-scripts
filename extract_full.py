import gzip, tarfile, io, os, zipfile
data=open(r"E:\tools\Install.PortMaster.sh",'rb').read()
gzs=[m.start() for m in __import__('re').finditer(rb'\x1f\x8b\x08', data)]
off=[g for g in gzs if g>27000][0]
blob=data[off:]
raw=gzip.decompress(blob)
tf=tarfile.open(fileobj=io.BytesIO(raw))
tmp=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\pm_extract"
os.makedirs(tmp,exist_ok=True)
for m in tf.getmembers():
    if m.isfile():
        out=os.path.join(tmp,os.path.basename(m.name))
        f=tf.extractfile(m); open(out,'wb').write(f.read())
        print("extracted:",m.name,"->",out,len(f) if False else os.path.getsize(out))
print("=== PortMaster.zip contents ===")
zf=zipfile.ZipFile(os.path.join(tmp,"PortMaster.zip"))
names=zf.namelist()
print("zip entries:",len(names))
# top-level dirs
tops=set(n.split('/')[0] for n in names)
print("top-level:",tops)
for n in names[:60]: print("  ",n)
print("=== installer.sh head ===")
print(open(os.path.join(tmp,"installer.sh"),encoding='utf-8',errors='replace').read()[:1500])
