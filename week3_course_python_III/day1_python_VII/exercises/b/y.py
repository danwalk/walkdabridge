import sys
classpath = 'C:\\Users\\Daniel\\Desktop\\The Bridge\\walkdabridge\\week3_course_python_III'
sys.path.append(classpath)

from day1_python_VII.exercises.a.x import f1x, f2x

vary1 = "yone"
vary2 = "ytwo"

def f1y():
    print("f1y")
    f1x()

def f2y():
    print("f2y")
    f2x()