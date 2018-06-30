#!/usr/bin/env python
procver = 'Linux version 4.17.0-rc4+ (likvidera@ubuntu) (gcc version 7.2.0 (Ubuntu 7.2.0-8ubuntu3.2)) #9 Sat May 12 12:57:01 PDT 2018'

const = [
    '40369e8c78b46122a4e813228ae8ee6e',
    'e4a75afe114e4483a46aaa20fe4e6ead',
    '8c3749214f4a9131ebc67e6c7a86d162'
]

new_const = []
for c in const:
    new_const.append(map(lambda x: int(x, 16), [c[i:i+2] for i in range(0, len(c), 2)]))

for c in new_const:
    raw = ''
    i = 0
    for k in c:
        raw += hex(ord(procver[i]) ^ k)[2:].rjust(2, '0')
        i += 1
    print raw