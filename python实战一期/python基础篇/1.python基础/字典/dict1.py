#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: dict1.py
@time: 2019/1/7 14:48
'''

# info = dict()
# name = input("Please enter your name: " )
# age = int(input("Please enter your age: "))
# gender = input("Please enter M/F: ")
# info['name'] = name
# info['age'] = age
# info['gender']= gender
# print(info)


# info = dict()
# name = input("Please enter your name: " )
# age = int(input("Please enter your age: "))
# gender = input("Please enter M/F: ")
# info['name'] = name
# info['age'] = age
# info['gender']= gender
# for i,j in info.items():
#     print(i,j)
# print('main end')


info = dict()
name = input("Please enter your name: " )
age = int(input("Please enter your age: "))
gender = input("Please enter M/F: ")
info['name'] = name
info['age'] = age
info['gender']= gender
for i,j in info.items():
    print("%s: %s" % (i,j))
print('main end')