#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 代码清单3-1.py
@time: 2018/12/27 16:10
'''

# 根据指定的宽度打印格式良好的价格列表

width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}} {{:>{}}}'.format(item_width,price_width)
fmt = '{{:{}}} {{:>{}.2f}}'.format(item_width,price_width)
print(header_fmt)
print(fmt)

print("=" * width)
print(header_fmt.format('Item','Price'))
print('-' * width)
print(fmt.format('Apples',0.4))
print(fmt.format('Pears',0.5))
print(fmt.format('Cantaloupes',1.92))
print(fmt.format('Dried Apricots (16 oz.)',8))
print(fmt.format('Prunes (4 lbs.)',12))
print('='* width)

