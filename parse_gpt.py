import struct
img=r"D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.img"
f=open(img,'rb')
# MBR / protective MBR at LBA0
f.seek(0)
mbr=f.read(512)
# check GPT signature "EFI PART" at LBA1 (offset 512)
f.seek(512)
sig=f.read(8)
print("GPT signature:", sig)
if sig==b'EFI PART':
    f.seek(512+24)
    # GPT header: entries start LBA (offset 72 in header? actually at +72)
    # GPT header layout: signature(8) rev(4) size(4) crc(4) reserved(4) current_lba(8) backup(8)
    # first_usable(8) last_usable(8) disk_guid(16) entries_start_lba(8) num_entries(4) ...
    f.seek(512+72)
    entries_lba=struct.unpack('<Q',f.read(8))[0]
    f.seek(512+80)
    num_entries=struct.unpack('<I',f.read(4))[0]
    entry_size=struct.unpack('<I',f.read(4))[0]
    print("entries_lba=%d num=%d entry_size=%d"%(entries_lba,num_entries,entry_size))
    f.seek(entries_lba*512)
    for i in range(num_entries):
        e=f.read(entry_size)
        if len(e)<128: break
        type_guid=e[0:16]
        first_lba=struct.unpack('<Q',e[32:40])[0]
        last_lba=struct.unpack('<Q',e[40:48])[0]
        name=e[56:128].decode('utf-16-le','replace').rstrip('\x00')
        if type_guid!=b'\x00'*16:
            print("Part %d: type=%s first=%d last=%d size=%dMB name=%s"%(i,type_guid.hex(),first_lba,last_lba,(last_lba-first_lba+1)*512//1048576,name))
else:
    # MBR: 4 entries at offset 446, each 16 bytes, partition type + LBA
    print("MBR-based")
    for i in range(4):
        e=mbr[446+i*16:446+i*16+16]
        status=e[0]; ptype=e[4]; start=struct.unpack('<I',e[8:12])[0]; sectors=struct.unpack('<I',e[12:16])[0]
        if ptype!=0:
            print("Part %d: type=0x%02x start_lba=%d size=%dMB"%(i,ptype,start,sectors*512//1048576))
f.close()
