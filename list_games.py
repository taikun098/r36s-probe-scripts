import re
g=open(r"E:\ports\gamelist.xml",encoding='utf-8').read()
names=re.findall(r'<name>(.*?)</name>',g)
names=sorted(set(names))
out=open(r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\all_ports.txt","w",encoding='utf-8')
out.write("TOTAL %d\n"%len(names))
for n in names:
    out.write(n+"\n")
out.close()
print("total",len(names),"-> written all_ports.txt")
