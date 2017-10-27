# -*- coding: utf-8 -*-

from functools import reduce

def addabs( x, y, f):
    return f(x) + f(y)

def f(x):
    return x*x

def add(x,y):
    return x+y

def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]


def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))


def str2int2(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))


def normalize(name):
    return name.title()

def prod(L):
    def mup(x,y):
        return x*y
    return reduce(mup,L)


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def fn(x,y):
        return x*10 + y
    i = s.index('.')
    # a1 = s[:i]
    # a2 = s[i+1:]

    return reduce(fn, list(map(char2num, s[:i]))) + (reduce(fn,list(map(char2num,s[i+1:])))*pow(10,-len(s[i+1:])))

    #return reduce(fn,map(char2num,s)) # reduce(fn,[1,5,7,9,0.1,1,2,3,4,])

def highorderfunc():
    print addabs(-5,7,abs)
    # map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    r = map(f,[1,2,3,4,5,6,7,8])
    print r
    print list(r)

    r = map(str,[1,2,3,4,5,6,7,8])
    print r
    # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    print reduce(add,[1,3,5,7,9])

    print reduce(fn,[1,2,3,4,5])

    print reduce(fn,map(char2num, '1579'))
    print(str2int('1579'))
    print(str2int2('1579'))


    L = ['adam', 'LISA', 'barT']
    print list(map(normalize,L))

    print("3579=",prod([3,5,7,9]))

    print str2float('1579.1234')
# 函数名也是变量




