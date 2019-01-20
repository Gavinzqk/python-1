#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 判断是否是数字.py
@time: 2019/1/14 17:45
'''
s = ''
def isNum(s):
    if not s.isdigit():
        return False
    return True

# a = ['a','1','2','b','333',33,44]
#
# for i in a:
#     if isNum(str(i)):
#         print(i)

print('\n'.join(' '.join('{0}*{1}={2}'.format(x,y,x*y) for x in range(1,1+y)) for y in range(1,10)))
