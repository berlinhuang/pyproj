# -*- coding: utf-8 -*-


def build(x,y):
    return lambda: x*x+y+y # return a anonymous function


def main():
    print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # 关键字lambda表示匿名函数，冒号前面的x表示函数参数
    print build(1,2)() #



