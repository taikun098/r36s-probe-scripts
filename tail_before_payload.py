data=open(r"E:\tools\Install.PortMaster.sh",'rb').read()
pk=23588166
# print text just before payload (last 4000 bytes before PK)
seg=data[pk-4000:pk]
try:
    s=seg.decode('utf-8',errors='replace')
except:
    s=seg.decode('latin-1',errors='replace')
print("=== script tail before payload ===")
print(s[-3000:])
