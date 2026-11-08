import os
base = r"E:\consoles"
print("=== panels ===")
for d in sorted(os.listdir(base)):
    p = os.path.join(base,d)
    if os.path.isdir(p) and d!='kernel':
        try:
            dtbs=[x for x in os.listdir(p) if x.endswith('.dtb')]
            print(f"{d}: {len(dtbs)} dtb(s) -> {dtbs[0] if dtbs else 'none'}")
        except Exception as e:
            print(d, "ERR", e)
print("=== kernel ===")
kp=os.path.join(base,'kernel')
if os.path.isdir(kp):
    for d in sorted(os.listdir(kp)):
        dp=os.path.join(kp,d)
        if os.path.isdir(dp):
            try:
                files=[x for x in os.listdir(dp)]
                print(f"{d}: {files}")
            except Exception as e:
                print(d,e)
