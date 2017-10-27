from distutils.core import setup

setup(
    name="base",
    version="001",
    description = "base grammar",
    author = "berlin",
    author_email = "berlinmail@qq.com",
    url = "https://github.com/berlinhuang/pyproj",
    keywords = "",
    license = "",
    packages = [],
    install_requires = [],

    entry_points ={
        'console_scripts':[
            'test = pyproj.base:main',
            'fileoperate = pyproj.start:main',
            'test = pyproj.main:main',
        ]
    }

)