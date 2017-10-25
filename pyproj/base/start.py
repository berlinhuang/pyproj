# -*- coding: utf-8 -*-

from pyproj.base import charencode
from pyproj.base import listtuple

def docharencode():
    charencode.ordchr()
    charencode.unicode()
    charencode.length()
    charencode.format()

def dolisttuple():
    listtuple.list()
    listtuple.tuple()







def main():
    docharencode()
    dolisttuple()


