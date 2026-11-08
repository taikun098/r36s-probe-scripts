import os
for p in [r"E:\consoles\k36s", r"E:\consoles\k36", r"E:\consoles\r36t"]:
    print("===", p, "exists:", os.path.isdir(p))
    if os.path.isdir(p):
        for e in os.listdir(p):
            fp=os.path.join(p,e)
            print("   ", e, ("DIR" if os.path.isdir(fp) else "%d bytes"%(os.path.getsize(fp) if os.path.isfile(fp) else 0)))
