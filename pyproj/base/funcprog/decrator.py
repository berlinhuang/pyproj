# -*- coding: utf-8 -*-


import functools

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper


# decorator本身需要传入参数 那就需要编写一个返回decorator的高阶函数
def log_param(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

def logger(func):
    @functools.wraps(func) # wrapper.__name__ = func.__name__
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

def logger_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw): #在定义wrapper()的前面加上@functools.wraps(func)
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator






def main():
    # @log   # 把@log放到now()函数的定义处，相当于执行了语句： now = log(now)

    def now():
        print('2015-02-15')
    now = log(now) #now:返回的wrapper()函数
    now()
    print now.__name__
    print "..............................."


    # @logger('execute') #返回的是decorator函数 再调用返回的函数，参数是now1函数，返回值最终是wrapper函数
    def now_param():
        print("2017-01-01")
    now_param = log_param('execute')(now_param) #
    now_param()
    print now_param.__name__

    print "..............................."







    def now1():
        print("2017-01-01")
    now1 = logger(now1)
    now1()
    print now1.__name__

    print "..............................."




    def now1_param():
        print("2014-05-15")

    now1_param = logger_param("execute")(now1_param)
    now1_param()
    print now1_param.__name__


