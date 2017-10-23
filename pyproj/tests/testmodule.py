
def getModuleAtrributes( modulename ):
    print("list module %s :" % modulename.__name__)
    for mem in dir(modulename):
        print("key: %s " % mem, "value: %s " % getattr(modulename, mem))
