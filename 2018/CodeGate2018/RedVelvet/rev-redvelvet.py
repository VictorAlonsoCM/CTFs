#!/usr/bin/python
#check http://solution-36.blogspot.com/2014/08/solving-picoctf-2013-harder-serial-with.html

from z3 import *
import os

solver = Solver()

a1 = BitVec('a1', 32) 
a2 = BitVec('a2', 32) 

#a1 = Int('s[0]')
#a2 = Int('s[1]')


solver.add(a1 > 85)
solver.add(a1 < 96 )

solver.add(a2 > 96)
solver.add(a1 < 112 )

solver.add(a1 * 2 * (a2 ^ a1) - a2 == 10858)

print("Solving...")
# Solve the equations
print(solver.check())
print(solver.model())
