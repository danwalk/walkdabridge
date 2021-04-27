import sys, os

path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.append(path)
print("Ruta y.py: -->", path)

import a.x as x

vary1 = "yone"
vary2 = "ytwo"

def f1y():
    print("f1y")
    x.f1x()

def f2y():
    print("f2y")
    x.f2x()

