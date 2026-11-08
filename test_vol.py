import os
out=[]
p = '\\\\?\\Volume{40ce8ada-c89d-11f1-b2f8-b4d5bdec0e5e}\\'
out.append('path=%s' % p)
out.append('exists=%s' % os.path.exists(p))
try:
    e=os.listdir(p)
    out.append('readable entries=%d' % len(e))
    for x in e[:20]:
        out.append('  '+x)
except Exception as ex:
    out.append('ERR %r' % ex)
r='C:\\Users\\user\\Doubao\\chats\\2026-10-15\\new-chat-2\\dtb_probe\\vol_out.txt'
open(r,'w').write('\n'.join(out))
print('written')
