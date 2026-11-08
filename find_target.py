data=open(r"E:\tools\Install.PortMaster.sh",'rb').read()
pk=23588166
# read the script-text portion just before payload (search for target dir logic)
seg=data[:pk]
# decode as latin-1 to find ascii strings
s=seg.decode('latin-1',errors='ignore')
import re
# find lines with target dirs
for m in re.finditer(r'[^\n]*(?:/roms|/opt|PortMaster|\.local|target|DESTDIR|INSTALL_DIR|dirname|cd |mkdir)[^\n]*', s):
    line=m.group(0).strip()
    if len(line)<300 and any(k in line for k in ['/roms','/opt','PortMaster','.local','DESTDIR','INSTALL','mkdir','control.txt','libs']):
        print(repr(line[:250]))
