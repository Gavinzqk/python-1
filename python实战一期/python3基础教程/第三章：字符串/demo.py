#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: demo.py
@time: 2018/12/27 11:37
'''
# import math
# print("{pi!s} {pi!r} {pi!a}".format(pi="π"))


# n= "The number is {num:d}".format(num=42)
# print(n)


# num = 0b111111
# print(num)


# n = "{num:10}".format(num="Bob")
# print(n)


# import math
# n = "Pi day is {pi:.2f}".format(pi=math.pi)
# print(n)


# n = "{:.8}".format("Guido van Rossum")
# print(n)


# n = 'One googol is {n:,}'.format(n=10**10)
# print(n)


# 左对齐，右对齐，居中可以使用 < > 和^
# from math import pi
# n = "{0:<10.2f} \n{0:^10.2f} \n{0:>10.2f}".format(pi)
# print(n)


# n = '{:$^15}'.format(' WIN BIG ')
# print(n)


# print("%s + %s = %s"  % (1,2,1+3))


# for i in range(1,10):
#     for j in range(1,i+1):
#         print( "%s*%s=%s" % (j,i,j*i),end=' ')
#     print()


# from math import pi
# print('{0:10.2f} \n{1:10.2f}'.format(pi,-pi))
# print('{0:-.2} \n{1:+.2}'.format(pi,-pi))
# print('{0:+.2} \n{1:+.2}'.format(pi,-pi))
# print('{0:.3} \n{1:.3}'.format(pi,-pi))


# n = '{:#g}'.format(43)
# print(n)


# n = '{:20} {:>10.2f}'.format('gavin',1990)
# print('*' * 30)
# print(n)

# import string
# n = string.digits
# a = string.ascii_letters
# b = string.ascii_uppercase
# c = string.ascii_lowercase
# d = string.printable
# e = string.punctuation
# print(n)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# n = ' A problem is a chance for you to do your best '
# print(n.center(60,'*'))
# print(n.find('ro'))
# a = (n.center(60,'-'))
# print(a.find('--',5,10))


# seq = ['1','2','3','4','5']
# sep = '+'
# print(sep.join(seq))
# dirs = ['usr','local','src']
# print('/'+'/'.join(dirs))
# print('C: ' + '\\' +'\\'.join(dirs))


# a = "Hello ,Gavin"
# if 'gavin'  in a.lower():
#     print('True')

# a = "Hello,world"
# print(a.replace('world','gavin'))

# a = ['a','b','c']
# b ='+'.join(a)
# print(b)
# print(b.split('+'))
# print(list('ab'))

# import math
# n = '{0:<+10.2f} \n{1:>10.2f}'.format(math.pi,- math.pi)
# print(n)
