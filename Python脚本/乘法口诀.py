#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 乘法口诀.py
@time: 2019/1/14 17:19
'''
for x in range(1,10):
    for y in range(1,x+1):
        print("%s*%s=%s" % (y,x,y*x),end=' ')
    print()