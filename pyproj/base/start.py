# -*- coding: utf-8 -*-

from pyproj.base import charencode
from pyproj.base import listtuple
from pyproj.base import condition as cond
from pyproj.base import loop
from pyproj.base import dictset

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


def main():
    # docharencode()
    # dolisttuple()
    # docondition()
    # doloop()
    dodictset()
