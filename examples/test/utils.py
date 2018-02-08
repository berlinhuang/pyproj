# -*- coding: utf-8 -*-
#import
#1 当前文件目录
#2 环境变量PYTHONPATH
#3 sys.path(list 类型)

import sys

from pyproj.utils import module_dbg, hello_world

os = __import__("os")

def hello():
    hello_world.sayhi()

def get_sys_help():
    module_dbg.getModHelp(sys)

def get_os_dir():
    module_dbg.getModDir(os)

def get_cur_module_attr():
    module_dbg.getModAttr(sys.modules[__name__]) #current module
    module_dbg.getModAttr(module_dbg) #specific module

def get_sys_path():
    for mem in sys.path:
        print mem


def main():
    # hello()
    # get_cur_module_attr()
    get_sys_help()
    get_os_dir()
    # get_sys_path()
    pass

