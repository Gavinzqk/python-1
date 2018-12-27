#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 切片.py
@time: 2018/12/25 11:25
'''
# 从类似于http://www.something.com的url中提取域名
url = input("please enter the URL: ")
domain = url [11: -4]
print("Domain name: " + domain)
