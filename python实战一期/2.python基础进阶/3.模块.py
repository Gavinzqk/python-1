#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 3.模块.py
@time: 2019/1/10 14:49
'''

#! /usr/bin/python

def wordCount(s):
    chars =len(s)
    words = len(s.split())
    lines = s.count('\n')
    print lines,words,chars

if __name__=='__main__':
    s = open('/root/passwd').read()
    wordCount(s)


# vim 2.py
