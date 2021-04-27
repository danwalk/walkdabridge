import sys, os

path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.append(path)
print("Ruta x.py: -->", path)

import b.c.z as z

varx1 = "xone"
varx2 = "xtwo"

def f1x():
    print("f1x")

def f2x():
    print("f2x")
    z.f2z()

f2x()