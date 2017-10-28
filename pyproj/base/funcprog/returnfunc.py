# -*- coding: utf-8 -*-


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# return a function
# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax =ax +n
        return ax
    return sum


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs # 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了

def count_rare():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs


def main():
    print lazy_sum(1,3,5,7,9)()

    f = lazy_sum(1,3,5,7,9)
    print f()

    f1 = lazy_sum(1, 3, 5, 7, 9)
    print f == f1

    f1, f2, f3 = count()
    print f1(),f2(),f3() #全部都是9 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3

    f1, f2, f3 = count_rare()
    print f1(),f2(),f3()