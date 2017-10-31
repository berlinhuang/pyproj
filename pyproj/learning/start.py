# -*- coding: utf-8 -*-

from pyproj.learning import charencode
from pyproj.learning import listtuple
from pyproj.learning import condition as cond
from pyproj.learning import loop
from pyproj.learning import dictset
from pyproj.learning.func import func

from pyproj.learning.advance import advance
from pyproj.learning.funcprog import funcprog

from pyproj.learning.module import usemodule
from pyproj.learning.object import object
from pyproj.learning.mysql import dataoperate

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
    # advance.advance()
    # funcprog.funcprog()
    # usemodule.test()
    # object.object()
    dataoperate.operate()