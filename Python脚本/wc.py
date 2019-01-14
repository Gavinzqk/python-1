#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: wc.py
@time: 2019/1/14 17:20
'''
# 脚本后面跟文件名，打印出文件有多少行、单词、字母

import sys
def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print(lines, words, chars)
try:
    if sys.argv[1]:
        try:
            with open(sys.argv[1]) as fd:
                s = fd.read()
        except:
            print('NO such file')
            sys.exit()
except:
    sys.exit()
wordCount(s)