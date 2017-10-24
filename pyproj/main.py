# -*- coding: utf-8 -*-

# 文件夹 package
# py文件 module


from pyproj.tests import test


if __name__ == "__main__":
    test.main()






# 所有的模块都有一个内置属性 __name__
# 如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名

# 直接运行py文件,则__name__的值是__main__
# import 一个.py文件后,__name__的值就不是'__main__'