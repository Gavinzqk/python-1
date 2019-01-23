#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: wc命令实现从标准输入.py
@time: 2019/1/23 18:16
'''

#! /usr/bin/python
import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-c', '--char',
                  dest='chars',
                  action='store_true',
                  default=False,
                  help='only count chars')
parser.add_option("-w", '--word',
                  dest='words',
                  action='store_true',
                  default=False,
                  help='only count words')
parser.add_option("-l", '--line',
                  dest='lines',
                  action='store_true',
                  default=False,
                  help='only count lines')

# parser.parse_args()返回的是元组，用两个变量接收里面的两个元素
options, args = parser.parse_args()

# 判断三个选项都没输入时，则赋值true
if not (options.lines or options.words or options.chars):
    options.lines,options.words,options.chars = True,True,True

data = sys.stdin.read()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

# 判断options接收的字典里对应的选项是否为true
if options.lines:
    print(lines,end=' ')
if options.words:
    print(words,end=' ')
if options.chars:
    print(chars)