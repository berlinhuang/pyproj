# -*- coding: utf-8 -*-

import math

def call():
    print abs(-1)
    print max(1, 2, 3, 4)

    print int('123')
    print int(12.32)

    print float('12.33')
    print (1.23)
    print bool(1)
    print bool(12)
    print bool(0)
    print bool('')

    # 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
    # return None可以简写为return


def pop():
    pass  #pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
    # 缺少了pass，代码运行就会有语法错误。

#函数执行完毕也没有return语句时，自动return None
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x





def move(x, y, step, angle = 0):
    nx = x +step*math.cos(angle)
    ny = x - step* math.sin(angle)
    return nx, ny


def returntuple():
    x, y = move(100, 100, 60, math.pi / 6)
    print x, y

    r = move(100, 100, 60, math.pi / 6)  # return a tuple
    print r



def power(x, n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s


def enroll(name, gender,age = 3, city= "xm"):
    print("name:",name)
    print ("gender:",gender)
    print("age",age)
    print("city",city)


# 传入一个list，添加一个END再返回
def add_end(L=[]):
    L.append("END")
    return L

def add_one_end( L = None ):
    if L is None:
        L =[]
    L.append("END")
    return L


def default_param():
    print power(3)
    print power(2, 3)
    enroll("berlin", "F")
    print add_end([1, 2, 3])
    print add_end(['x', 'y', 'z'])
    print add_end()
    print add_end()  # 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list
    print add_one_end()
    print add_one_end()


def calc(numbers): # list
    sum = 0
    for n in numbers:
        sum = sum+ n*n
    return sum


def calc_param_chg(*nums): # changeable param
    sum = 0
    for n in nums:
        sum = sum+ n*n
    return sum


def param_chg():
    print calc([1,2,3,4,])
    nums = [1,2,3,4]
    print calc(nums)

    print calc_param_chg(*nums)
    print calc_param_chg(1,2,3,4)
    print calc_param_chg()


def person(name,age,**kw):
    print ('name:',name,"age:",age,"other:",kw)




def key_word_param():
    person('Michael', 30)
    person('Bob', 35, city='Taipei')
    person('Adam', 45, gender='M', job='Engineer')

    extra = {'city':'Beijing','job':'Engineer'} # dict
    person('Jack', 24, city = extra['city'], job = extra['job'])
    person('Jack', 24, **extra)
    # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
    # kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


def person_check(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print ('name:',name,"age:",age,"other:",kw)


# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# def named_person(name, age, *, city, job):
#     print(name,age,city,job)


# 如果函数定义中已经有了一个可变参数*args，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
# def person(name, age, *arg, city, job):
#     print(name, age, city, job)






def named_key_word_param():
    person_check('Jack', 24, city='Beijing', addr='chaoyang',zipcode=123456)
    # named_person('Jack', 24, city='Beijing', job='Engineer')

def func():
    call()
    pop()
    # my_abs("s")
    returntuple()
    default_param()
    param_chg()
    key_word_param()
    named_key_word_param()

# 函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数*arg、命名关键字参数和关键字参数**kw。




# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！


# 要注意定义可变参数和关键字参数的语法:
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict

'''
调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数


'''
