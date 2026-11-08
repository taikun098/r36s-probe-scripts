import re
data=open(r"L:\rk3326-g80ca-linux.dtb",'rb').read()
strs=re.findall(rb'[\x20-\x7e]{5,}', data)
seen=set()
for s in strs:
    t=s.decode('ascii',errors='ignore')
    low=t.lower()
    if any(x in low for x in ['panel','st7703','sitronix','simple-panel','compatible','g80c','ilitek','hx8394','jd9365','rk3326']):
        if t not in seen:
            seen.add(t); print(t)
