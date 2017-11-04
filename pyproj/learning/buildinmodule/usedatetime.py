# -*- coding: utf-8 -*-

from datetime import datetime
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

from datetime import timedelta

# from datetime import timezone

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
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') # 2015-06-01 18:19:59
    print(cday)

def datetime_to_str():
    now = datetime.now()
    print( now.strftime('%a, %b %d %H:%M')) # Fri, Nov 03 17:07

def time_delta():
    now = datetime.now()
    print ("now: %s" % now)
    cday = datetime(2015,5,17,16,57,3,540997)
    print ("cday: %s" % cday)
    print ("now + 10 hours : %s" % (now + timedelta(hours = 10)))
    print ("now - 1 day: %s" % (now - timedelta( days = 1)))
    print ("now + 2 day 12 hours: %s" % (now + timedelta(days = 2, hours=12)))


'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
'''

def local_to_utc():
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00
    print('UTC+0:00 now =', utc_dt)

    # astimezone()将转换时区为北京时间:
    utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print('UTC+8:00 now =', utc8_dt)

def main():
    # get_curtime()
    # get_spectime()
    # to_timestamp()
    # to_datatime()
    str_to_datetime()
    # datetime_to_str()
    # time_delta()
