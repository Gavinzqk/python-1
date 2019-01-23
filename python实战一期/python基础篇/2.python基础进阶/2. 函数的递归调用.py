#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 2. 函数的递归调用.py
@time: 2019/1/9 16:37
'''

# def factorial(n):
#     sum = 1
#     for i in range(1,n+1):
#         sum *= i
#     return sum
# print(factorial(5)




# def factorial(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum +=i
#     print(sum)
# factorial(100)




# def factorial(n):
#     if n == 0:
#         return 0
#     else:
#         return n + factorial(n-1)
# print(factorial(100))


import sys
sys.setrecursionlimit(1000000)
def factorail(n):
    if n == 0:
        return 0
    else:
        return n + factorail(n-1)

print(factorail(1000))