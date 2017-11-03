# -*- coding: utf-8 -*-


import os, time, random

# multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pool
'''
Process：创建进程的类
daemon：将进程设为守护进程
Lock：处理多个进程间共享资源的问题，（多个进程共享一个锁）
Semaphore：用来控制对共享资源的访问数量，例如池的最大连接数。（最多同时能运行多少个进程）
Event：用来实现进程间同步通信。（解决共享数据操作导致数据不一致问题）

Queue：实现多进程之间的数据传递（生产者消费者模型）
Pipe：通信管道

Pool：可以提供指定数量的进程（和Queue类似，都是管理生成和销毁的关系，Pool管理进程，Queue管理数据）
'''
import subprocess



def do_fork():
    print("Process(%s) start..." % os.getpid())

    pid = os.fork()

    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))



def multiprocessing():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))   #
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')



def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def pooled_processing():
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：p = Pool(5) 就可以同时跑5个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#  apply_async(func,(args,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')



def do_subprocess():
    print('$ nslookup www.4399.com')
    r = subprocess.call(['nslookup','wwww.4399.com'])
    print('Exit code',r)
    # subprocess模块定义了一个类： Popen
    p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')# 如果子进程还需要输入，则可以通过communicate()方法输入
    print(output.decode('utf-8'))
    print('Exit code:',p.returncode)

def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while(True):
        value = q.get(True)
        print('Get %s from queue'% value )

def do_queue():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()  # 等待pw结束
    pr.terminate() # pr进程里是死循环，无法等待其结束，只能强行终止:





















