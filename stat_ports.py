import os
root=r"E:\ports"
n=0; sz=0
for dirpath,dirs,files in os.walk(root):
    for f in files:
        fp=os.path.join(dirpath,f)
        try: sz+=os.path.getsize(fp)
        except: pass
        n+=1
print("E:\\ports files=%d size=%.2f GB"%(n,sz/1e9))
