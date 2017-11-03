# -*- coding: utf-8 -*-

import multiprocess
import multithread
import threadlocal

def domultithread():
    multithread.multi_threading()
    multithread.do_lock()

def domultiprocess():
    multiprocess.do_fork()
    multiprocess.multiprocessing()
    multiprocess.pooled_processing()
    multiprocess.do_subprocess()
    multiprocess.do_queue()


def main():
    # domultiprocess()
    # domultithread()
    threadlocal.threadlocal()
