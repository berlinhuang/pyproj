# -*- coding: utf-8 -*-

from collections import Iterable

def iter():
    d = {'a':1,'b':2,'c':3}
    for key in d:
        print key,d[key]


    for value in d.values():
        print value


    for k,v in d.items():
        print k,v

    for ch in 'ABC':
        print ch

    print isinstance('abc', Iterable)
    print isinstance([1,2,3],Iterable)
    print isinstance(123,Iterable)

    for i,v in enumerate(['A','B','C','D']):
        print i,v

    for x,y in [(1,1),(2,3),(3,9)]:
        print x,y
