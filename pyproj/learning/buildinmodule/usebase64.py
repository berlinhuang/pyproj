# -*- coding: utf-8 -*-

# Base64是一种用 64个字符 来表示 任意二进制数据 的方法

import  base64

def main():

    # s = base64.b64decode(("在Python中使用BASE 64编码").encode("utf-8"))
    # print(s)
    # d = base64.b64decode(s).decode('utf-8')
    # print(d)
    #
    # s = base64.urlsafe_b64encode("在Python中使用BASE 64编码".encode('utf8'))
    # print(s)
    # d = base64.urlsafe_b64decode(s).decode('utf-8')
    # print(d)

    print(base64.b64encode(b'binary\x00string'))
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

    print( base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print( base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print( base64.urlsafe_b64decode('abcd--__'))
    pass

