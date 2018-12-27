#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 代码清单2-4.py
@time: 2018/12/25 13:58
'''
database = [
    ['albert', '1234'],
    ['laoba', '1234'],
    ['gavin', '4242'],
    ['smith', '7524']
]
username = input('User name: ')
pin = input('Pin code: ')
if [username, pin] in database:
    print('Access granted')
else:
    print("False")
