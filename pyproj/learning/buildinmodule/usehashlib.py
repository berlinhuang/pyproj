# -*- coding: utf-8 -*-

import hashlib

def main():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8')) # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())