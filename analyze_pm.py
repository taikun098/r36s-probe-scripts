import re
data=open(r"E:\tools\Install.PortMaster.sh",'rb').read()
print("file size:",len(data))
# 1) find tail -n + offset markers (makeself style)
for m in re.finditer(rb'tail -n \+(\d+)', data[:200000]):
    print("tail -n +",m.group(1).decode(),"at",m.start())
# 2) find script-logic tail: look for last occurrence of known shell keywords before payload
# 3) find tar/ustar magic or gzip magic
gzs=[m.start() for m in re.finditer(rb'\x1f\x8b\x08', data)]
print("gzip magic positions:",gzs[:20],"count",len(gzs))
# 4) find ASCII script boundary: scan where high-entropy binary starts
# print some text around first gzip
i=28727
print("=== around 28727 (gzip) ===")
print(repr(data[i-200:i+120]))
# 5) find 'label:' occurrences
print("label:", [m.start() for m in re.finditer(rb'label', data)])
# 6) find 'ARCHIVE'
print("archive:", [m.start() for m in re.finditer(rb'ARCHIVE', data)])
# 7) find last readable shell line before payload — search for 'CRCsum' context
print("=== text near end of script logic: search 'UMASK'/'help'/'echo' last ===")
for kw in [b'extract', b'UNTAR', b'makeself', b'umask', b'--gzip', b'--tgz', b'--target']:
    print(kw, [m.start() for m in re.finditer(re.escape(kw), data[:23588166])][-3:])
