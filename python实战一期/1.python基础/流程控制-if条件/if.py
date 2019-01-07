#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: if.py
@time: 2019/1/7 15:00
'''

# if 1 :
#     print('Hello,world')
# else:
#     print("It's false")


# if 1>2:
#     print('Hello,world')
# else:
#     print("It's false")


# score = int(input("Please enter a number: "))
#
# if score >= 90:
#     print('A: very good')
# elif score >=80:
#     print('B: good')
# elif score >=60:
#     print('Pass')
# else:
#     print('Not pass')



# yn = input("Please input yes/no: ")
# yn =yn.lower()
# if yn=='yes' or yn == 'y':
#     print("program is running")
# elif yn=='n' or yn=='no':
#     print('program is exist')
# else:
#     print("Please input yes/no")


yn = input("Please input yes/no: ")
yn = yn.lower()
yes = ('yes','y')
no = ('no','n')
if yn in yes:
    print("Program is running")
elif yn in no:
    print("Program is exist")
else:
    print("Please input yes/no: ")



