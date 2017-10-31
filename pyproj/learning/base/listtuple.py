# -*- coding: utf-8 -*-

def list():
    classmates = ['Micheal','Bob', 'Tracu']
    print classmates
    print "0",classmates[0]
    print "2",classmates[2]
    print "-1",classmates[-1]
    print len(classmates)
    classmates.append("Adam")
    print classmates
    classmates.insert(1,'jack')
    print classmates
    print "pop:",classmates.pop()
    print classmates
    classmates[1] = 'Sarah'
    print classmates


    L = ['Apple', 123, True]
    print L

    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print "s:",s
    print "len(s):",len(s)

    p = ['asp', 'php']
    t = ['python', 'java', p, 'scheme']
    print t


def tuple():
    classmates = ('Michael', 'Bob', 'Tracy')# tuple不可变，所以代码更安全
    print classmates
 
    t = (1)
    print t

    t = (1,)
    print t

    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    print t

