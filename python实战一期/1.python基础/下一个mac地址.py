#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 下一个mac地址.py
@time: 2019/1/8 14:49
'''
mac = '52:54:00:0c:9f:0f'
front_mac = mac[:-2]
last_mac = mac[-2:]
n = int(last_mac,16) + 1
if len(hex(n)[2:]) == 1:
    new_last_mac = '0' + hex(n)[2:]
else:
    new_last_mac =  hex(n)[2:]
next_mac = front_mac + new_last_mac
print(next_mac)