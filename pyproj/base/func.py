# -*- coding: utf-8 -*-

import math

def call():
    print abs(-1)
    print max(1, 2, 3, 4)

    print int('123')
    print int(12.32)

    print float('12.33')
    print (1.23)
    print bool(1)
    print bool(12)
    print bool(0)
    print bool('')

    # 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
    # return None可以简写为return


def pop():
    pass  #pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
    # 缺少了pass，代码运行就会有语法错误。

#函数执行完毕也没有return语句时，自动return None
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x

def move(x, y, step, angle = 0):
    nx = x +step*math.cos(angle)
    ny = x - step* math.sin(angle)
    return nx, ny


def returntuple():
    x, y = move(100, 100, 60, math.pi / 6)
    print x, y

    r = move(100, 100, 60, math.pi / 6)  # return a tuple
    print r


def power(x, n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s


def enroll(name, gender,age = 3, city= "xm"):
    print("name:",name)
    print ("gender:",gender)
    print("age",age)
    print("city",city)






def func():
    call()
    pop()
    #my_abs("s")
    returntuple()
    print power(3)
    print power(2,3)
    enroll("berlin","F")

















