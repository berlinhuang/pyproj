# -*- coding: utf-8 -*-
#import
#1 当前文件目录
#2 环境变量PYTHONPATH
#3 sys.path(list 类型)

from pyproj.tests import testmodule
from pyproj.tests import helloworld
import  sys, os

def hello():
    helloworld.sayhi()

def gethelp():
    testmodule.getModuleHelp(sys)

def getdir():
    testmodule.getModuleDir(sys)

def module():
    testmodule.getModuleAtrributes(sys.modules[__name__]) #current module
    testmodule.getModuleAtrributes(testmodule) #specific module

def getsyspath():
    for mem in sys.path:
        print mem


def main():
    # hello()
    # module()
    # gethelp()
    # getdir()
    getsyspath()

