# -*- coding: utf-8 -*-


import functools


def int2func(x, base=2):
    return int(x, base)



def main():
    print int('12345')

    print int('12345',base=8) #做N进制的转换
    print int('12345',16)

    print int2func('1000000')


    # functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
    int2 = functools.partial(int, base =2)
    print int2('1000000')

    kw = {'base': 2}
    print int('10010', **kw)

    max2 = functools.partial(max, 10)
    print max2(5,6,7) #实际上会把10作为*args的一部分自动加到左边，也就是：args = (10, 5, 6, 7) , max(*args)















