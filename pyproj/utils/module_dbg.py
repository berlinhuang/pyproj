# -*- coding: utf-8 -*-

def getModAttr( modulename ):
    print("####################module [%s] key, getattr(key):#####################" % modulename.__name__)
    for mem in dir(modulename):
        print("key: %s " % mem, "value: %s " % getattr(modulename, mem))

def getModHelp( modulename ):
    help(modulename)


def getModDir( modulename ):
    print("####################module [%s] Mem:#####################" % modulename.__name__)
    for mem in dir(modulename):
        print mem