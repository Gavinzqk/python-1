#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 统计剩余的内存.py
@time: 2019/1/8 15:35
'''

with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal'):
            total = line.split()[1]
        elif line.startswith('MemFree'):
            free = line.split()[1]
persent = '%.2f' % (float(free)/float(total)*100) + '%'
print('Free Size: ' + '%.2f' % (float(free)/1024) + 'M')
print('Free%: ' + persent)