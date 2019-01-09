#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 打印目录下所有文件.py
@time: 2019/1/9 18:23
'''

#! /usr/bin/python
import sys
import os
def printFile(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path,i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path,i))]

    for d in dirs:
        printFile(os.path.join(path,d))
    for f in files:
        print(os.path.join(path,f))

printFile(sys.argv[1])