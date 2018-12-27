#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 代码清单2-3.py
@time: 2018/12/25 13:11
'''
# 在位于屏幕中央且宽度合适的方框内打印一个句子
sentence = input("sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) //2
print()
print(' ' *  left_margin + '+' + '-' * (box_width -2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '|' + sentence + '|')
print(' '* left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '-' *(box_width-2) + '+')

print()