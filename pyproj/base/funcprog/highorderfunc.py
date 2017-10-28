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


def is_odd(n):
    return n%2 == 1

def not_empty(s):
    return s and s.strip()


def _odd_iter(): # 注意这是一个生成器，并且是一个无限序列 3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n): # 筛选函数
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _odd_iter()# 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) # 构造新序列

def by_name(t):
    return str.lower(t[0])

def by_score(t):
    return t[1]

# FIXME: the cmp param seems to be cancelled in python3
# def comp(t1,t2):
#     if t1[0]==t2[0]:
#         return t1[1]<t2[1]
#     else:
#         return t1[0]>t2[0]

def highorderfunc():
    # 函数名也是变量
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


    print list(filter(is_odd,[1,2,4,5,6,9,10,15]))
    print list(filter(not_empty,['A','','B',None,'C','']))


    # for n in primes():
    #     if n < 20:
    #         print n
    #     else:
    #         break

    print sorted([36,5,-12,9,-21])

    print sorted([36,5,-12,9,-21],key = abs)

    print sorted(['bob','about','Zoo','Credit'])

    print sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower )

    print sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True )

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88),('Lisa', 81)]
    print sorted( L, key = by_name) # 第一维度升序
    print sorted( L, key = lambda x:(x[0],x[1])) # 第一维度升序，第二维度也是升来排序
    print sorted( L, key = lambda x:(x[0],x[1]), reverse=True)  # 第一维度逆序，第二维度也是逆序排序

    # print sorted( L, cmp=comp)

