#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 类的属性总结.py
@time: 2019/1/11 11:34
'''
var = "函数的全局变量"
class MyClass(object):
    var1 = "类的公有属性"
    __var2 = "类的私有属性"

    def func1(self):
        self.var3 = "对象的公有属性"
        self.__var4 = "对象的私有属性"
        var5 = "函数的局部变量"
        print(var5)

    def func2(self):
        print(var)
        print(self.var1)
        print(self.__var2)
        print(self.var3)
        print(self.__var4)


# print(var)
# c = MyClass()
# c.func1()
# print(c.var1)
# print(c._MyClass__var2)
# print(c.var3)
# print(c._MyClass__var4)
# print(c.func1

c = MyClass()
c.func1()
print('*' * 30)
c.func2()
print('-' *30)
print(c.__dict__)
print()
print(MyClass.__dict__)
