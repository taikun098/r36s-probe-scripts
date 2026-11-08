import os
root=r"E:\ports"
shs=sorted(f for f in os.listdir(root) if f.endswith('.sh'))
print("root .sh count:",len(shs))
# build gamelist.xml
lines=['<?xml version="1.0" encoding="UTF-8"?>','<gameList>']
for f in shs:
    name=os.path.splitext(f)[0]
    path='./'+f
    lines.append('  <game>')
    lines.append('    <path>%s</path>'%path)
    lines.append('    <name>%s</name>'%name)
    lines.append('    <desc></desc>')
    lines.append('  </game>')
lines.append('</gameList>')
out=os.path.join(root,'gamelist.xml')
open(out,'w',encoding='utf-8').write('\n'.join(lines))
print("written",out)
print("gamelist.xml size:",os.path.getsize(out),"bytes, entries:",len(shs))
