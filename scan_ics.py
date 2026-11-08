import re, os, glob
# scan all ArkOS panel dtb for panel IC strings
roots = [r"E:\consoles"]
ic_kw = re.compile(rb'st770|hx839|il9881|ilitek|otm|nt355|rm671|rk611|sitronix|boe|jd9365|kd070|jm|tianma|cpt|jnc|display-ic|st7701|st7703|hx8394|hx8399|nt35510|rm69330|jd9365|pdi|jk', re.I)
results = {}
for root in roots:
    for dtb in glob.glob(os.path.join(root, "**", "*.dtb"), recursive=True):
        b = open(dtb, 'rb').read()
        strs = re.findall(rb'[\x20-\x7e]{4,}', b)
        ics = set()
        for x in strs:
            if ic_kw.search(x):
                ics.add(x.decode('latin1'))
        panel = os.path.basename(os.path.dirname(dtb))
        results[panel] = sorted(ics)

# print summary: which panels contain st770 / sitronix
print("=== panels matching st770/sitronix ===")
for panel, ics in sorted(results.items()):
    st = [i for i in ics if re.search(r'st770|sitronix', i)]
    if st:
        print(f"{panel}: {st}")

print()
print("=== ALL detected IC strings per panel (compact) ===")
for panel, ics in sorted(results.items()):
    if ics:
        print(f"{panel}: {ics}")
