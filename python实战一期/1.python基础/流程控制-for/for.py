#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: for.py
@time: 2019/1/7 15:38
'''

# dic = dict.fromkeys("abcde",100)
# for i in dic:
#     print(i)


# dic = dict(name='gavin',age=29)
# for k in dic:
#     print("%s: %s" % (k,dic[k]))


# dic = dict(name='gavin',age=29)
# for k in dic:
#     print("%s--->%s" % (k,dic[k]),end=' ')


# dic = dict(name='gavin',age=29)
# for k in dic.items():
#     print(k)


# dic = dict(name='gavin',age=29)
# for x,y in dic.items():
#     print("%s: %s" % (x,y))

# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%s*%s=%s" % (y,x,y*x),end=' ')
#     print()



# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)


# import random
# ran = random.randint(1,20)
# for i in range(1,7):
#     num = int(input("please input a number: "))
#     if num == ran:
#         print('你赢了')
#         break
#     else:
#         if num >ran:
#             if 6-i != 0: print("太大了")
#         elif num <ran:
#             if 6-i != 0: print("太小了")
# else:
#     print('你输了')



# import random
# ran = random.randint(1,20)
# for i in range(1,7):
#     while True:
#         num = input("please input a number: ")
#         if num.isdigit():
#             break
#         else:
#             continue
#     num = int(num)
#     if num == ran:
#         print("you win")
#         break
#     else:
#         if num > ran:
#             if 6-i !=0 :print('too large')
#             if 6 - i != 0: print('you have '+ str(6-i) + ' test')
#         elif num < ran:
#             if 6 - i != 0: print('too small')
#             if 6 - i != 0: print('you have ' + str(6-i) + ' test')
# else:
#     print('you lose')


# for i in range(1,5):
#     if i == 3:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print('main end')


# import sys
# for i in range(1,11):
#     if i == 3:
#         continue
#     if i == 8:
#         sys.exit()
#     print(i)
# else:
#     print('end')



# import time
# for i in range(1,10):
#     print(i)
#     time.sleep(1)
# else:
#     print('main end')
