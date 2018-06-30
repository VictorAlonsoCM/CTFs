import hashlib
from pwn import *
proc_version = "Linux version 4.17.0-rc4+ (likvidera@ubuntu) (gcc version 7.2.0 (Ubuntu 7.2.0-8ubuntu3.2)) #9 Sat May 12 12:57:01 PDT 2018"
# obtained from cat /proc/version within the kernel given
keys = ["40369e8c78b46122a4e813228ae8ee6e", "e4a75afe114e4483a46aaa20fe4e6ead", "8c3749214f4a9131ebc67e6c7a86d162"]

def get_hashes():
    ret = []
    for i in xrange(0,3):
        one_hashes = ""
        hex_data = keys[i].decode("hex")
        for i in xrange(0,len(hex_data)):
            one_hashes += chr(ord(proc_version[i]) ^ ord(hex_data[i]))
        ret.append(one_hashes)
    return ret

def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.digest()

hashes = get_hashes()
for i in xrange(0, 3):
    print "".join("{:02x}".format(ord(c)) for c in hashes[i])
# MD5 hashes
# 0c5ff0f900941747d69b7a4de4c8da40
# a8ce348b696e32e6d619c34f906e5a83
# c05e2754376ae75499b5170314a6e54c