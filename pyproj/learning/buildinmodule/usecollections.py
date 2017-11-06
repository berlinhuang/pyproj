# -*- coding: utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

def donamedtuple():
    Point = namedtuple('Point', ['x', 'y']) # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    p = Point(1, 2)
    print ('Point:',p.x, p.y)

    Circle = namedtuple('Circle',['x','y','r'])


# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素

def dodeque():
    q = deque(['a','b','c'])
    q.append('x')
    q.appendleft('y')
    print(q)


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
def dodefaultdict():
    dd = defaultdict(lambda:"N/A")
    dd['key1'] = 'abc'
    print('dd[\'key1\']=', dd['key1'])
    print('dd[\'key2\']=', dd['key2'])


'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict：
'''
def doOrderedDict():
    d = dict([('a',1),('b',2),('c',3)])
    print(d)

    od = OrderedDict([('a',1),('b',2),('c',3)])
    print(od)


# Counter是一个简单的计数器，例如，统计字符出现的个数
def doCounter():
    c= Counter()
    for ch in 'programming':
        c[ch] =  c[ch] + 1
    print c
    # OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.poitem(last = False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key,value))
        else:
            print('ad:',(key,value))
        OrderedDict.__setitem__(self,key,value)


def main():
    donamedtuple()
    dodeque()
    dodefaultdict()
    doOrderedDict()
    doCounter()
