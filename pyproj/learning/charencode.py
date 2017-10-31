# -*- coding: utf-8 -*-

def ordchr():
    print ord("A")
    #print ord('中')

    print chr(66)
    #print chr(25991)


# 对bytes类型的数据用带b前缀的单引号或双引号表示

def unicode():
    print 'ABC'.encode('ascii')
    # print '中文'.encode('utf-8')
    print b'ABC'.decode('ascii')
    print b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

def length():
    print len('ABC')
    print len(b'ABC')
    print len('中文')
    #print len('中文'.encode('utf-8'))

def format():
    print "hello, %s" % "world"
    print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
    print '%2d-%02d' % (3, 1)
    print '%.2f' % 3.1415926
    print 'Age: %s. Gender: %s' % (25, True)
    print 'growth rate: %d %%' % 7
    #print '中文'.encode('gb2312')