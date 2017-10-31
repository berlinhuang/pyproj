# -*- coding: utf-8

from pyproj.learning.base import charencode
from pyproj.learning.base import condition as cond
from pyproj.learning.base import dictset
from pyproj.learning.base import loop
from pyproj.learning.base import listtuple



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
     docharencode()
     dolisttuple()
     docondition()
     doloop()
     dodictset()
