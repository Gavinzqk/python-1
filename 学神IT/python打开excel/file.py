#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: file.py
@time: 2019/2/14 11:06
'''

import xlwt
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = workbook.add_sheet('test', cell_overwrite_ok=True)

with open('cpuinfo') as f:
    lines = f.readlines()
    for index,line in enumerate(lines):
        lineSplit = line.split(':')
        if len(lineSplit)==2:
            key,value = lineSplit
            key = key.strip()
            value = value.strip()
            sheet.write(index,0,key)
            sheet.write(index,1,value)

workbook.save('cpu.xls')