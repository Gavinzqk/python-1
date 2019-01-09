#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: while.py
@time: 2019/1/8 9:49
'''


# num = 0
# while True:
#     num += 1
#     if num == 5:
#         break
#     else:
#         print(num)



# num = 0
# while not num == 5:
#     num +=1
#     print(num)


# while 1:
#     a = input("please input something(q for exit): ")
#     if a == 'q':
#         break
#     else:
#         print('hello')


a = ''
q = ['quit','q','QUIT','Q']
while a not in q:
    a = input("please input something(q for exit): ")
    print('hello')
    if not a:
        break
else:
    print('main end')






