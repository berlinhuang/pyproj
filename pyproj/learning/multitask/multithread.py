# -*- coding: utf-8 -*-

import time,threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def multi_threading():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放
        lock.acquire() # # 先要获取锁:
        try:
            change_it(n)
        finally:
            lock.release()


def do_lock():
    t1 = threading.Thread(target = run_thread, args = (5,))
    t2 = threading.Thread(target = run_thread, args = (8,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(balance)