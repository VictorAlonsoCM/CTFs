#!/usr/bin/python

from z3 import *
import os

s = Solver()
for i in range(1,27):
	globals()['v%i'%i]=BitVec('v%i'%i,32)

#func1
s.add(v1 * 2 * (v2 ^ v1) - v2 == 10858)
s.add(v1 > 85, v1 <= 95)
s.add(v2 > 96, v2 <= 111)

#func2
s.add(v2 % v3 == 7)
s.add(v3 > 90)

#func3
s.add(v3 / v4 + (v4 ^ v3) == 21)
s.add(v3 <= 99)
s.add(v4 <= 119)

#func4
s.add(v5==95)

#func5
#s.add((v6 + v5) ^ (v5 ^ v6 ^ v5) == 225)
s.add((v6 + v5) ^ (v5 ^ v6 ^ v5) == 225)
s.add(v5 > 90)
s.add(v6 <= 89)

#func6
s.add(v6 <= v7)
s.add(v7 <= v8)
s.add(v6 > 85)
s.add(v7 > 110)
s.add(v8 > 115)
s.add((v7 + v8) ^ (v6 + v7) == 44)
s.add((v7 + v8) % v6 + v7 == 161)

#func7
s.add(v8 >= v9)
s.add(v9 >= v10)
s.add(v8 <= 119)
s.add(v9 > 90)
s.add(v10 <= 89)
s.add((v8 + v10) ^ (v9 + v10) == 122)
s.add((v8 + v10) % v9 + v10 == 101)

#func8
s.add(v10 <= v11)
s.add(v11 <= v12)
s.add(v12 <= 114)
s.add((v10 + v11) / v12 * v11 == 97)
s.add((v12 ^ (v10 - v11)) * v11 == -10088)

#func9
s.add(v12 == v13)
s.add(v13 >= v14)
s.add(v14 <= 99)
s.add(v14 + v12 * (v14 - v13) - v12 == -1443)

#func10
s.add(v14 >= v15)
s.add(v15 >= v16)
s.add(v15 * (v14 + v16 + 1) - v16 == 15514)
s.add(v15 > 90)
s.add(v15 <= 99)

#func11
s.add(v17 >= v16)
s.add(v16 >= v18)
s.add(v17 > 100, v17 <= 104)
#s.add(v17 <= 104)
s.add(v16 + (v17 ^ (v17 - v18)) - v18 == 70)
s.add((v17 + v18) / v16 + v16 == 68)

#func12
s.add(v18 >= v19)
s.add(v19 >= v20)
s.add(v19 <= 59)
s.add(v20 <= 44)
s.add(v18 + (v19 ^ (v20 + v19)) - v20 == 111)
s.add((v19 ^ (v19 - v20)) + v19 == 101)

#func13
s.add(v20 <= v21)
s.add(v21 <= v22)
s.add(v20 > 40)
s.add(v21 > 90)
s.add(v22 <= 109)
s.add(v22 + (v21 ^ (v22 + v20)) - v20 == 269)
s.add((v22 ^ (v21 - v20)) + v21 == 185)

#func14
s.add(v22 >= v24)
s.add(v23 >= v24)
s.add(v23 <= 99)
s.add(v24 > 90)
s.add(v22 + (v23 ^ (v23 + v22)) - v24 == 185)

#func15
s.add(v25 >= v26)
s.add(v25 >= v24)
s.add(v26 > 95)
s.add(v25 <= 109)
s.add(((v25 - v24) * v25 ^ v26) - v24 == 1214)
s.add(((v26 - v25) * v26 ^ v24) + v25 == -1034)

print("Solving...")
# Solve the equations
if (s.check() == sat):
 values =s.model()
 flag=""
 for i in range(1,27):
  obj = globals()['v%i' % i]
  char = values[obj].as_long()
  flag += chr(char)
 print flag


#Flag = What_You_Wanna_Be?:)_lc_la <==Change "c" with "a" ==> (la_la) !
