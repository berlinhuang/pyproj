# -*- coding: utf-8 -*-


import types

def fn():
    pass


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x


class Student(object):
    def __init__(self,name):
        self.name = name

    name = 'Student' # Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所




def objtype():
    print type(fn) == types.FunctionType
    print type(abs)==types.BuiltinFunctionType
    print type(lambda x:x)==types.LambdaType
    print type((x for x in range(10)))== types.GeneratorType

    print isinstance('a',str)
    print isinstance(123,int)
    print isinstance(b'a',bytes)
    print isinstance([1,2,4],(list,tuple)) #判断一个变量是否是某些类型中的一种
    print "MyObject===================="
    obj = MyObject()
    print hasattr(obj,'x')
    print hasattr(obj,'y')
    setattr(obj, 'y', 19) # 设置一个属性'y
    print hasattr(obj,'y')
    print getattr(obj,'y')
    print getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404
    print hasattr(obj,'power')

    func = getattr(obj,'power')
    print func()

    s = Student('Bob')
    s.score = 10

    print s.name
    print Student.name
    s.name = 'Michael'
    print s.name
    print Student.name
    del s.name # 如果删除实例的name属性
    print s.name # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

