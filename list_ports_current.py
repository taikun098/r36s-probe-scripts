import os
dst=r'\\?\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\ports'
out=[]
if os.path.isdir(dst):
    entries=os.listdir(dst)
    shs=[f for f in entries if f.endswith('.sh')]
    dirs=[d for d in entries if os.path.isdir(os.path.join(dst,d))]
    out.append('ports root .sh: %d'%len(shs))
    out.append('ports root dirs: %d'%len(dirs))
    out.append('--- all .sh ---')
    for f in sorted(shs): out.append('  '+f)
    out.append('--- dirs (first 80) ---')
    for d in sorted(dirs)[:80]: out.append('  '+d)
    # red alert check
    ra=[x for x in entries if any(k in x.lower() for k in ['red','alert','ra','cnc','command','vanilla','openra'])]
    out.append('--- red-alert/cc candidates ---')
    for x in ra: out.append('  '+x)
    out.append('PortMaster dir present: %s'%os.path.isdir(os.path.join(dst,'PortMaster')))
else:
    out.append('ports dir NOT FOUND at volume')
r=r'C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\ports_current.txt'
open(r,'w',encoding='utf-8').write('\n'.join(out))
print('done')
