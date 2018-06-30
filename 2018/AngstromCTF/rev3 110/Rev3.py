from z3 import *

b = "egzloxi|ixw]dkSe]dzSzccShejSi^3q"
s = Solver()
for i in range(1,33):
	globals()['a%i'%i]=BitVec('a%i'%i,32)

#func1
s.add((a1 ^ 9) - 3 == 101)
s.add((a2 ^ 9) - 3 == 103)
s.add((a3 ^ 9) - 3 == 122)
s.add((a4 ^ 9) - 3 == 108)
s.add((a5 ^ 9) - 3 == 111)
s.add((a6 ^ 9) - 3 == 120)
s.add((a7 ^ 9) - 3 == 105)
s.add((a8 ^ 9) - 3 == 124)
s.add((a9 ^ 9) - 3 == 105)
s.add((a10 ^ 9) - 3 == 120)
s.add((a11 ^ 9) - 3 == 119)
s.add((a12 ^ 9) - 3 == 93)
s.add((a13 ^ 9) - 3 == 100)
s.add((a14 ^ 9) - 3 == 107)
s.add((a15 ^ 9) - 3 == 83)
s.add((a16 ^ 9) - 3 == 101)
s.add((a17 ^ 9) - 3 == 93)
s.add((a18 ^ 9) - 3 == 100)
s.add((a19 ^ 9) - 3 == 122)
s.add((a20 ^ 9) - 3 == 83)
s.add((a21 ^ 9) - 3 == 122)
s.add((a22 ^ 9) - 3 == 99)
s.add((a23 ^ 9) - 3 == 99)
s.add((a24 ^ 9) - 3 == 83)
s.add((a25 ^ 9) - 3 == 104)
s.add((a26 ^ 9) - 3 == 101)
s.add((a27 ^ 9) - 3 == 106)
s.add((a28 ^ 9) - 3 == 83)
s.add((a29 ^ 9) - 3 == 105)
s.add((a30 ^ 9) - 3 == 94)
s.add((a31 ^ 9) - 3 == 51)
s.add((a32 ^ 9) - 3 == 113)

print("Solving...")
# Solve the equations
if (s.check() == sat):
 values =s.model()
 flag=""
 for i in range(1,33):
  obj = globals()['a%i' % i]
  char = values[obj].as_long()
  flag += chr(char)
 print flag
 #final flag = actf{reversing_aint_too_bad_eh?}