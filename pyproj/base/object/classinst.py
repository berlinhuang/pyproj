# -*- coding: utf-8 -*-


class Student(object):
    pass


def objStu():
    bart = Student()
    print bart
    bart.name = 'Bart Simpson'
    print bart.name


class Stu2(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(std):
        print('%s:%s' % (std.name,std.score))

    def get_grade(self):
        if self.score > 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return 'C'


def objStu2():
    bart = Stu2('Bart Simpson',59)
    bart.print_score()
    print bart.get_grade()



class Stu3(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score)) # 对于外部代码来说，无法从外部访问实例变量.__name和实例变量.__score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


def objStu3():
    bart = Stu3('Bart Simpson',59)
    bart.print_score()
    #print bart.__name__ #以__开头，就变成了一个私有变量（private），只有内部可以访问






class Animal(object):
    def __init__(self):
        pass
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def __init__(self):
        pass
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def __init__(self):
        pass
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()

def objAni():
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()
    l = list()
    a = Animal()
    d = Dog()
    print isinstance(l,list)
    print isinstance(a,Animal)
    print isinstance(d, Dog)
    print isinstance(d, Animal)
    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run() 方法
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    run_twice(Animal())
    run_twice(Dog())














def obj():
    objStu()
    objStu2()
    objStu3()
    objAni()
