#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 类的方法总结.py
@time: 2019/1/12 3:09 PM

'''

class MyClass(object):

    name = 'Test'

    def func1(self):
        print(self.name,end=' ')
        print("类的公有方法")

    def __func2(self):
        print(self.name, end=' ')
        print("类的私有方法")

    @classmethod
    def classFun(self):
        print(self.name, end=' ')
        print("类方法")

    @staticmethod
    def staticFun():
        print(MyClass.name, end=' ')
        print("类的静态方法")


    def __init__(self):
        self.func1()
        self.__func2()
        self.classFun()
        self.staticFun()

c = MyClass()
print('-' * 50)
MyClass.classFun()
MyClass.staticFun()
