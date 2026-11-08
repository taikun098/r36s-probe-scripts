import os, glob
from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(p):
    return FdtBlobParse(open(p,'rb')).to_fdt()

# load ST7703 init from orig
orig = load(base + r"\evb_orig.dtb")
op = orig.resolve_path('/dsi@ff450000/panel@0')
st7703_init = None
for it in op.subdata:
    if isinstance(it,FdtProperty) and it.get_name()=='panel-init-sequence':
        st7703_init = list(it.bytes)
print("ST7703 init len:", len(st7703_init))

# scan all ArkOS panel dtb
results = []
for dtb in glob.glob(os.path.join(r"E:\consoles", "**", "*.dtb"), recursive=True):
    try:
        f = load(dtb)
        p = f.resolve_path('/dsi@ff450000/panel@0')
    except Exception as e:
        continue
    init = None
    for it in p.subdata:
        if isinstance(it,FdtProperty) and it.get_name()=='panel-init-sequence':
            if hasattr(it,'bytes'):
                init = list(it.bytes)
            elif hasattr(it,'words'):
                # words -> little-endian bytes
                init = []
                for w in it.words:
                    v = w & 0xffffffff
                    init += [v & 0xff, (v>>8)&0xff, (v>>16)&0xff, (v>>24)&0xff]
            break
    if init is None:
        continue
    panel = os.path.basename(os.path.dirname(dtb))
    # compare: byte equality ratio
    if st7703_init:
        n = min(len(init), len(st7703_init))
        same = sum(1 for i in range(n) if (init[i]&0xff)==(st7703_init[i]&0xff))
        ratio = same / max(len(st7703_init),1)
        # leading bytes match
        lead = 0
        for i in range(min(len(init), len(st7703_init))):
            if (init[i]&0xff)==(st7703_init[i]&0xff): lead+=1
            else: break
        results.append((ratio, lead, len(init), panel))

results.sort(key=lambda x:-x[0])
print("top 30 by overall byte-match ratio (ratio, leading_match, init_len, panel):")
for r in results[:30]:
    print(r)
