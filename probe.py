import re, glob
kw = re.compile(r'panel|st770|hx839|il9881|ilitek|otm|nt355|rm671|rk611|sitronix|boe|jd9365|qled|panel-timing|timing|jancolor|lcd|display|dsi|lvds|rgb|edp|backlight', re.I)
for f in sorted(glob.glob('*.dtb')):
    b = open(f, 'rb').read()
    strs = re.findall(rb'[\x20-\x7e]{4,}', b)
    s = set()
    for x in strs:
        d = x.decode('latin1')
        if kw.search(d):
            s.add(d)
    print('=' * 18, f)
    for x in sorted(s):
        print('  ', x)
    print()
