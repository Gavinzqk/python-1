#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 类的内置方法.py
@time: 2019/1/11 11:23
'''

import gc
class People(object):
    color = 'yellow'

    def students(self):
        print('I am a student')

    def test(self):
        self.fd = open('file.txt')
        for i in self.fd.readlines():
            print(i,end='')

    def __str__(self):
        return 'This is class People'

    class Chinese(object):
        name = "I am Chinese"
        def fun(self):
            print(self.name)
        def __str__(self):
            return "This is class Chinese"

    # def __del__(self):
    #     self.fd.close()

    def __init__(self,c='black'):
        self.color = c

    def __del__(self):
        print('end')

ren = People()
gavin = ren.Chinese()
print(ren)
print(ren.color)
print(People.color)
print(gc.collect())




