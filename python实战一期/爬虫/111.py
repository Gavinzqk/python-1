#! /usr/bin/env python

'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 111.py
@time: 2019/1/17 12:14
'''

str_data = '''ch: beauty
  sn: 120
  listtype: new
  temp: 1
  '''

for data in str_data.splitlines():
    line_data = data.split(': ')
    print(line_data)