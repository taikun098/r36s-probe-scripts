import struct
img=r"D:\R36S_backup_20261015\extract\dArkOS_G80CA-RE_trixie_02062026.img"
part_start=237568*512  # bytes
part_size=7500*1024*1024
f=open(img,'rb')
f.seek(part_start+1024)
sb=f.read(1024)
magic=struct.unpack('<H',sb[56:58])[0]
print("ext4 magic=0x%04x"%(magic))
if magic!=0xEF53:
    print("NOT ext4"); f.close(); exit()
blocks_count=struct.unpack('<I',sb[4:8])[0]
log_block_size=struct.unpack('<I',sb[24:28])[0]
block_size=1024<<log_block_size
blocks_per_group=struct.unpack('<I',sb[32:36])[0]
inodes_per_group=struct.unpack('<I',sb[40:44])[0]
inode_size=struct.unpack('<H',sb[88:90])[0]
rev=struct.unpack('<I',sb[76:80])[0]
first_ino=struct.unpack('<I',sb[84:88])[0]
desc_size=struct.unpack('<H',sb[254:256])[0] if len(sb)>254 else 32
print("block_size=%d blocks_per_group=%d inodes_per_group=%d inode_size=%d rev=%d first_ino=%d desc_size=%d"%(
    block_size,blocks_per_group,inodes_per_group,inode_size,rev,first_ino,desc_size))
f.close()
