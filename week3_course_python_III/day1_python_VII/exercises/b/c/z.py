import sys, os

path = __file__
for i in range(3):
    path = os.path.dirname(path)
sys.path.append(path)
print("Ruta z.py: -->", path)

import a.x as t
import b.y as q

varz1 = "zone"
varz2 = "ztwo"

def f1z():
    print("f1z")
    q.f1y()

def f2z():
    print("f2z")
    t.f2x()

