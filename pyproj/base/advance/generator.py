# -*- coding: utf-8 -*-


def fib(max):
    print "begin fib"
    n, a, b = 0,0,1
    while n< max:
        print b
        a, b = b, a+b
        n = n + 1
    return 'done fib'


def fibyield(max):
    print "begin fib"
    n, a, b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    # return 'done fib'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# 杨辉三角


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [ L[i] + L[i+1] for i in range(len(L)-1)] + [1]

# 杨辉三角

def tri(num):
    n, a = 0, [1]
    while n < num:
        yield a
        a = [ x + y for x, y in zip(a +[0], [0] + a) ]
        n+=1
    # return "finish"



def generate():
    L = [x * x for x in range(10)] # L是一个list
    print L

    g = (x * x for x in range(10)) # g是一个generator
    print g
    for n in g:
        print n

    print fib(6)

    o= odd()
    print next(o)
    print next(o)
    print next(o)
    # next(o) # 第4次调用next(o)就报错

    # g = fibyield(6)
    # while True:
    #     try:
    #         x = next(g)
    #         print('g:',x)
    #         # print "g:", next(g)
    #     except StopIteration as e:
    #         print('Generator return value:', e.value)
    #         break

    n = 0
    for t in triangles():
        print t
        n += 1
        if n>10:
            break

    for i in tri(11):
        print i


# generator和函数的执行流程不一样
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

