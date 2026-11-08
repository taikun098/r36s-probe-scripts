import os, subprocess
print("E: exists:", os.path.exists("E:\\"))
# check disk3 via diskpart-free method: use wmic or registry
# simpler: list logical volumes via ctypes
try:
    import ctypes
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for i in range(26):
        if bitmask & (1 << i):
            drives.append(chr(65+i)+":\\")
    print("logical drives:", drives)
except Exception as e:
    print("err", e)
