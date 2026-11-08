import os
out=r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\diag_2048tree.txt"
L=[]
d=r"E:\ports\2048"
def tree(base,indent=""):
    for n in sorted(os.listdir(base)):
        fp=os.path.join(base,n)
        sz = os.path.getsize(fp) if os.path.isfile(fp) else "dir"
        L.append("%s  %s  (%s)"%(indent,n,sz))
        if os.path.isdir(fp):
            tree(fp,indent+"    ")
L.append("=== E:\\ports\\2048 full tree ===")
tree(d)
# control.txt key variables
c=open(r"E:\ports\PortMaster\control.txt",encoding='utf-8',errors='replace').read()
L.append("="*30+" control.txt key vars "+"="*30)
for kw in ["CFW_NAME","DEVICE_ARCH","GPTOKEYB","gptokeyb","directory=","platform"]:
    for line in c.splitlines():
        if kw in line and not line.strip().startswith("#"):
            L.append("  "+line.strip())
L.append("="*30+" mod_.txt head "+"="*30)
m=open(r"E:\ports\PortMaster\mod_.txt",encoding='utf-8',errors='replace').read()
L.append(m[:1200])
open(out,"w",encoding='utf-8').write("\n".join(L))
print("written",out,len(L),"lines")
