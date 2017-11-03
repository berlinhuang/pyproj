# -*- coding: utf-8 -*-

from datetime import datetime
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

def get_curtime():
    now = datetime.now() # datetime.now()返回当前日期和时间，其类型是datetime
    print now
    print type(now)


def get_spectime():
    dt = datetime(2015, 4, 14, 15, 21)
    print (dt)

# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time, 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

'''
你可以认为：
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是：
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
'''

def to_timestamp():
    dt = datetime(2015, 4, 14, 15, 21)
    # print(dt.timestamp())

def to_datatime():
    t = 1429417200.0
    print("local time(beijing = utc+8): ")
    print (datetime.fromtimestamp(t))  # 本地时间
    print("utc time: ")
    print (datetime.utcfromtimestamp(t))  # UTC时间

def str_to_datetime():
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

def datetime_to_str():
    now = datetime.now()
    print( now.strftime('%a, %b %d %H:%M'))


def main():
    get_curtime()
    get_spectime()
    to_timestamp()
    to_datatime()
    str_to_datetime()
    datetime_to_str()

