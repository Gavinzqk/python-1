#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: python版wc命令.py
@time: 2019/1/24 12:26 AM

'''
#! /usr/bin/python
import sys
import os
from optparse import OptionParser

def opt():
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
    return options,args


def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines,words,chars

def print_wc(options,lines,words,chars,fn):
    # 判断options接收的字典里对应的选项是否为true
    if options.lines:
        print(lines,end=' ')
    if options.words:
        print(words,end=' ')
    if options.chars:
        print(chars,end=' ')
    print(fn)

def main():
    options,args = opt()

    # 判断三个选项都没输入时，则赋值true
    if not (options.lines or options.words or options.chars):
        options.lines,options.words,options.chars = True,True,True

    if args:
        # 当文件有多个时循环读取统计，最后相加打印一行total
        total_lines,total_words,total_chars = 0,0,0
        for fn in args:
            # 判断文件是否非文件
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                lines,words,chars = get_count(data)
                print_wc(options,lines,words,chars,fn)
                total_lines += lines
                total_words += words
                total_chars += chars
            elif os.path.isdir(fn):
                # 此处用sys.stderr.write() 方法是为了错误重定向，print是标准输出
                sys.stderr.write('%s: is a directory\n' % fn)
            else:
                # 2> /dev/null 时不打印错误信息
                sys.stderr.write('%s: No such file or directory\n' % fn)
        if len(args) >1:
            print_wc(options,total_lines,total_words,total_chars,'total')

    else:
        data = sys.stdin.read()
        fn = ''
        lines,words,chars = get_count(data)
        print_wc(options,lines,words,chars,fn)

if __name__ == '__main__':
    main()
