# -*- coding: utf-8 -*-

import itertools

def main():
    ns = itertools.repeat('ABC',3)
    for n in ns:
        print(n)


    nat = itertools.count(1)
    for n in nat:
        print n
        if n >= 100:
            break

    cs = itertools.cycle('ABC')
    t = 10
    for c in cs:
        print(c)
        t = t-1
        if t==0:
            break

    nat = itertools.count(1)
    ns = itertools.takewhile(lambda x:x<=10,nat)
    print(list(ns))

    for c in itertools.chain("ABC",'xyz'): #可以把一组迭代对象串联起来，形成一个更大的迭代器
        print(c)

    for key, group in itertools.groupby('ABBCCAAA'):# groupby()把迭代器中相邻的重复元素挑出来放在一起：
        print(key, list(group))

    for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        print(key, list(group))
