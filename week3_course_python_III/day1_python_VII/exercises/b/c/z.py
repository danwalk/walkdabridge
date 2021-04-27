import sys
classpath = 'C:\\Users\\Daniel\\Desktop\\The Bridge\\walkdabridge\\week3_course_python_III'
sys.path.append(classpath)

from day1_python_VII.exercises.a.x import f2x
from day1_python_VII.exercises.b.y import f1y

varz1 = "zone"
varz2 = "ztwo"

def f1z():
    print("f1z")
    f1y()

def f2z():
    print("f2z")
    f2x()

