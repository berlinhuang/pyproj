# -*- coding: utf-8 -*-

def getModuleAtrributes( modulename ):
    print("list module %s :" % modulename.__name__)
    for mem in dir(modulename):
        print("key: %s " % mem, "value: %s " % getattr(modulename, mem))

def getModuleHelp( modulename ):
    help(modulename)


def getModuleDir( modulename ):
    for mem in dir(modulename):
        print mem