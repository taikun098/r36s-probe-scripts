import os
p=r"E:\ports"
games=[d for d in os.listdir(p) if os.path.isdir(os.path.join(p,d))]
withsh=0; nopath=0
for g in games:
    gp=os.path.join(p,g)
    has_sh=any(f.endswith(".sh") for f in os.listdir(gp))
    if has_sh: withsh+=1
    else: nopath+=1
print("E:\\ports total games:",len(games))
print("with .sh launcher:",withsh)
print("without .sh:",nopath)
if nopath:
    print("examples without .sh:",[d for d in games if not any(f.endswith('.sh') for f in os.listdir(os.path.join(p,d)))][:10])
# count .sh in ports_scripts
ps=os.listdir(r"E:\ports_scripts")
print("ports_scripts items:",len(ps),"sh:",sum(1 for f in ps if f.endswith('.sh')))
