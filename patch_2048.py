import os
f=r'E:\ports\2048\2048.sh'
s=open(f,encoding='utf-8',errors='replace').read()
diag='''{
echo "===2048-diag==="
echo "CFW_NAME=$CFW_NAME"
echo "DEVICE_ARCH=$DEVICE_ARCH"
echo "controlfolder=$controlfolder"
echo "directory=$directory"
echo "GAMEDIR=$GAMEDIR"
echo "raloc=$raloc"
echo "GPTOKEYB=$GPTOKEYB"
echo "HAS_retroarch_local=$(ls /usr/local/bin/retroarch 2>&1)"
echo "HAS_retroarch_bin=$(ls /usr/bin/retroarch 2>&1)"
echo "HAS_retroarch_opt=$(ls /opt/retroarch/bin/retroarch 2>&1)"
} > /roms/2048_error.txt 2>&1
'''
if '===2048-diag===' in s:
    print('already patched')
else:
    s=s.replace('source $controlfolder/control.txt\n','source $controlfolder/control.txt\n'+diag,1)
s=s.replace('$raloc/retroarch $raconf -L $GAMEDIR/2048_libretro.so.${DEVICE_ARCH}',
            '$raloc/retroarch $raconf -L $GAMEDIR/2048_libretro.so.${DEVICE_ARCH} 2>>/roms/2048_error.txt')
open(f,'w',encoding='utf-8',newline='').write(s)
print('patched OK, size',os.path.getsize(f))
