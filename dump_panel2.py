from pyfdt.pyfdt import FdtBlobParse, FdtNode, FdtProperty

base = r"C:\Users\user\Doubao\chats\2026-10-15\new-chat-2\dtb_probe"

def load(path):
    with open(path, 'rb') as fh:
        return FdtBlobParse(fh).to_fdt()

def fmt_raw(raw):
    if isinstance(raw, str):
        # already a string
        s = raw
        if len(s) < 80:
            return repr(s)
        return s[:80]+'...'
    try:
        s = raw.decode('ascii')
        if all(c.isprintable() for c in s):
            return repr(s)
    except Exception:
        pass
    return raw.hex()

def dump_props(node, indent='  '):
    for item in node.subdata:
        if isinstance(item, FdtProperty):
            try:
                raw = item.to_raw()
            except Exception as e:
                raw = b'<err>'
            print(indent + "PROP %-28s = %s" % (item.get_name(), fmt_raw(raw)))

for tag, path in [("ARKOS", base+r"\origin_p1.dtb"), ("ORIG", base+r"\evb_orig.dtb")]:
    f = load(path)
    p = f.resolve_path('/dsi@ff450000/panel@0')
    print("="*30, tag, "panel@0")
    dump_props(p)
    # display-timings
    for sub in p.subdata:
        if isinstance(sub, FdtNode) and sub.get_name().startswith('display-timings'):
            print("  [display-timings]")
            dump_props(sub, '    ')
            for sub2 in sub.subdata:
                if isinstance(sub2, FdtNode):
                    print("    [%s]" % sub2.get_name())
                    dump_props(sub2, '      ')
    print()
