#https://www.pwndiary.com/write-ups/angstrom-ctf-2018-product-key-write-up-reverse200/
#!/usr/bin/env python
#https://ctftime.org/event/577/tasks/
def swapArr(L, i, j):
    L[i], L[j] = L[j], L[i]
 
pad = [0x77, 0x3C, 0x1E, 0x6B, 0x39, 0x13, 0x22, 0x0F, 0x24, 0x2, 0x73, 0x59, 0x67, 0x64, 0x21, 0x73, 0x17, 0x1E, 0x6D, 0x5B, 0x4, 0x66, 0x65, 0x51, 0x5B, 0x43, 0x57, 0x27, 0x0E, 0x6A, 0x0F, 0x6D, 0x2F, 0x1, 0x48, 0x44, 0x3B, 0x48, 0x5E, 0x80, 0x4E, 0x1F, 0x27, 0x11, 0x33, 0x46, 0x33, 0x4A, 0x25, 0x5E, 0x33, 0x32, 0x28, 0x60, 0x6E, 0x0, 0x6, 0x1F, 0x28, 0x67, 0x43, 0x7D, 0x57, 0x32]
 
name = [ord(x) for x in "Artemis Tosini"]
email = [ord(x) for x in "artemis.tosini@example.com"]
emailPadding = 32 - len(email)
namePadding = 32 - len(name)
 
name += pad[emailPadding:emailPadding + namePadding]
email += pad[:emailPadding]
 
for i in xrange(32):
    name[i] ^= 0xF;
    email[i] ^= 0x5;
 
values = [0, 0, 0, 0, 0, 0]
values[0] = sum(email[0:10])
values[1] = sum(email[10:25])
values[2] = sum(email[25:32])
values[3] = sum(name[0:13])
values[4] = sum(name[13:20])
values[5] = sum(name[20:32])
    
for i, val in enumerate([2, 4, 6, 8, 7, 5]):
    values[i] = values[i] * val % 10000
 
for i in xrange(6):
    values[i] -= email[4 * i] % name[4 * i + 2]
 
for i in xrange(6):
    values[i] -= sum(email)
    values[i] -= sum(name)
 
swapArr(values, 4, 5)
swapArr(values, 0, 5)
swapArr(values, 2, 3)
swapArr(values, 1, 5)
swapArr(values, 2, 5)
swapArr(values, 3, 4)
 
for i in xrange(6):
    values[i] -= 4 * (sum(name[0:32:2]) - sum(name[1:32:2]))
    values[i] += sum(email[i+1:32:i+2]) * sum(email[0:32:i+2]) % 10000
 

serial = '-'.join('{:0>4}'.format(x) for x in values)
print serial