# -*- coding: utf-8 -*-

from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

############################################

class Query_s(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name )

@contextmanager # 这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
def create_query(name):
    print('Begin')
    q = Query_s(name)
    yield q
    print('End')


#############################################

@contextmanager

def tag(name):
    print("<%s>" %name)
    yield
    print("<%s>" %name)


'''
with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
'''
##############################################

#
# from contextlib import closing
# from urllib.request import urlopen
#
#
# # closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
# '''
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()
# '''
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)





def main():
    with Query('Bob') as q:
        q.query()

    with create_query('Bob') as q:
        q.query()

    with tag('h1'):
        print("hello")
        print("world")