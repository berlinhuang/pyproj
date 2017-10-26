# -*- coding: utf-8 -*-

from pyproj.base import charencode
from pyproj.base import listtuple
from pyproj.base import condition as cond
from pyproj.base import loop
from pyproj.base import dictset
from pyproj.base.func import func

from pyproj.base.advance import advance

def docharencode():
    charencode.ordchr()
    charencode.unicode()
    charencode.length()
    charencode.format()

def dolisttuple():
    listtuple.list()
    listtuple.tuple()


def docondition():
    cond.ifcond()

def doloop():
    loop.loop()

def dodictset():
    dictset.dict()
    dictset.testset()
    dictset.obj()


def main():
    # docharencode()
    # dolisttuple()
    # docondition()
    # doloop()
    # dodictset()
    # func()
    advance.advance()