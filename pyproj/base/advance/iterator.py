# -*- coding: utf-8 -*-

# for 循环的数据类型
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
from collections import Iterable
from collections import Iterator
def iter():
    # 可迭代对象
    print "Iterable:"
    print isinstance([],Iterable)
    print isinstance({},Iterable)
    print isinstance('abc',Iterable)
    print isinstance((x for x in range(10)),Iterable)
    print isinstance(100,Iterable)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象
    # Iterator对象
    print "Iterator:"
    print isinstance((x for x in range(10)),Iterator)
    print isinstance([], Iterator)
    print isinstance({}, Iterator)
    print isinstance('abc',Iterator)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
    print "iter():"
    # print isinstance(iter([]), Iterator)
    # print isinstance(iter('abc'),Iterator)


    # Python的for循环本质上就是通过不断调用next()函数实现的
    for x in [1,2,3,4,5]:
        pass

    #实际上完全等价于：

    it = iter([1,2,3,4,5])
    while True:
        try:
            x = next(it)
        except StopIteration:
            break