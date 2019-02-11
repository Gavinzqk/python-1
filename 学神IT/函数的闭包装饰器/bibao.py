#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: bibao.py
@time: 2019/1/31 14:46
'''

# def outer(num): # 外部函数
#     def inner(num_in): # 内嵌函数
#         print('inner,num_in is %d' % num_in)
#         return num_in +num
#     return inner
#
# a = outer(20)
# print(a(10))


'''
x = 2
def outer():
    x = 0
    def inner():
        global x  # global调用的全局变量x = 2
        x = x+1
        print(x)
    return inner
f = outer()
f()  # x= 3，全局变量也变成了x=3
#或者
outer()()#inner()  在x= 3 的基础上又执行了一次函数，变成了x = 4
print(x)  # 全局变量 x = 4

'''


# def func1():
#     print('this is xuegod1')
# def Dec(func):
#     def inner():
#         func()
#         print('I come form china')
#     return inner
# f1 = Dec(func1)
# f1()
#
#
#
# def Dec(func):
#     def inner():
#         func()
#         print('I come form china')
#     return inner
# @Dec
# def func1():
#     print('this is xuegod1')
# func1()



# import time
# a = ['gavin','zhang']
#
# def outer(func):
#     def inner(name):
#         func(name)
#         print('开始判断你有没有登陆权限')
#         time.sleep(2)
#         if name in a:
#             print('登录成功')
#             time.sleep(1)
#         else:
#             print('你没有权限，无法登录')
#             time.sleep(1)
#     return inner
# @outer
# def login(name):
#     print('我要浏览')
#
# login('g')

x = 1

def outer():
    def inner():
        print(x)
    return inner

a = outer()
a()