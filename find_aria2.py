import os, glob
roots = [r"C:\Program Files", r"C:\Program Files (x86)", "C:\\", "D:\\", os.path.expandvars(r"%LOCALAPPDATA%"), os.path.expandvars(r"%USERPROFILE%")]
found=[]
scanned=0
for r in roots:
    if not os.path.isdir(r): continue
    for dirpath, dirnames, filenames in os.walk(r):
        # skip slow system dirs
        dl=dirpath.lower()
        if any(x in dl for x in [r'\windows', r'\$recycle', 'node_modules', r'\system volume']):
            dirnames[:]=[]
            continue
        if 'aria2' in [f.lower() for f in filenames]:
            found.append(os.path.join(dirpath,[f for f in filenames if f.lower()=='aria2c.exe'][0]))
        scanned+=1
        if scanned>40000: break
    if scanned>40000: break
print("FOUND aria2c:")
for f in found: print("  ", f)
print("total scanned dirs:", scanned)
