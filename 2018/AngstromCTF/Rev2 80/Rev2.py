from z3 import *

s = Solver()
a1 = BitVec('a1', 32) 
a2 = BitVec('a2', 32) 
#func1
s.add(a1 > 9, a1 <= 99)
s.add(a2 <= 99, a2 > 9, a1 <= a2)
s.add(a1 * a2 == 3431)

print("Solving...")
# Solve the equations
print(s.check())
print(s.model())