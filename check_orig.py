import sys
p = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe\evb_orig.dtb"
b = open(p, 'rb').read()
print("size:", len(b))
print("magic:", b[:4].hex())
# find strings of interest
import re
kw = re.compile(r'panel|st770|hx839|il9881|ilitek|otm|nt355|rm671|rk611|sitronix|boe|jd9365|qled|simple-panel|compatible|G80|RF35|board|Model', re.I)
strs = re.findall(rb'[\x20-\x7e]{4,}', b)
s = set()
for x in strs:
    d = x.decode('latin1')
    if kw.search(d):
        s.add(d)
for x in sorted(s):
    print(" ", x)
