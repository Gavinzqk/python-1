#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 类的继承.py
@time: 2019/1/11 15:01
'''

# class People(object):
#     color = 'yellow'
#
#     def think(self):
#         self.wdell = 'Earth'
#         print('I am a thinker')
#
#     def __init__(self):
#         self.color = 'white'
#     # def __str__(self):
#     #     return 'This is People class'
#
# class Martian(object):
#
#     def __int__(self):
#         print('I am from Martian')
#         self.color = 'red'
#
#
# class Chinese(People,Martian):
#     def __init__(self):
#         Martian.__init__(self)
#
#
#
# cn = Chinese()
# print(cn)







class Martian(object):
    color = 'red'

    def __init__(self):
        self.dwell= 'Martian'

    def test(self):
        print(self.color)

class People(object):
    def __init__(self):
        self.dwell = 'Earth'
        self.color = 'yellow'

    def think(self):
        print('I am a %s' % self.color)
        print('My home is %s' % self.dwell)

class Chinese(Martian,People):
    def __init__(self):
        People.__init__(self)

    def talk(self):
        print('I like talking')

cn = Chinese()
cn.think()
cn.talk()
cn.test()