#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 1. 函数.py
@time: 2019/1/9 10:48
'''



# def fun():
#     print('hello world')
#
# fun()




# def fun(x):
#     try:
#         if type(int(x)) == type(1):
#             return 1
#     except:
#         return 0
#
# while True:
#     num1 = input("please input the first number: ")
#     if not fun(num1):
#         print("it's not a number ")
#         continue
#     num2 = input("please input the seacond number: ")
#     if not fun(num2):
#         print("it's not a number ")
#         continue
#     else:
#         break
# num1 = int(num1)
# num2 = int(num2)
# print("%s+%s=%s" % (num1,num2,num1+num2))
# print("%s-%s=%s" % (num1,num2,num1-num2))
# print("%s*%s=%s" % (num1,num2,num1*num2))
# print("%s/%s=%.2f" % (num1,num2,num1/num2))




# #! /usr/bin/python
# import sys
# def isNumber(x):
#     for i in x:
#         if i in '012345678':
#             pass
#         else:
#             print('%s is not a number' % x)
#             sys.exit()
#     else:
#         print('%s is a number' % x)
# isNumber(sys.argv[1])




# 打印进程pid
#! /usr/bin/python
# import os
# import sys
# def isNum(x):
#     for i in x:
#         if i not in '0123456789':
#             break
#     else:
#         return 1
#
# for y in os.listdir('/proc'):
#     if isNum(y):
#         print(y)


# y = 1
# def fun():
#     global y,x
#     x = 2
#     y += 1
#     print(x)
#     print(y)
# fun()
# print(x)



# x = 1
# def fun():
#     global x
#     x += 1
# fun()
# print(x)

# def fun():
#     global y
#     y = 'ab'
# fun()
# print (y + 'cd')



# def fun():
#     global x
#     x = 1
#     #print(locals())
# fun()
# print(locals())




# def fun():
#     print('hello world')
# print(fun())



# def fun():
#     print('hello world')
#     return 1
# print(fun())



# 打印pid
#! /usr/bin/python
# import os
# import sys
# def isNum(x):
#     if x.isdigit():
#         return 1
# for i in os.listdir('/proc'):
#     if isNum(i):
#         print(i)


