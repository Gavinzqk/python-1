#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 协程2_greenlet.py
@time: 2019/1/30 10:14
'''
import time,greenlet
def work1():
    for i in range(5):
        print('work1')
        time.sleep(0.2)
        g2.switch()

def work2():
    for i in range(5):
        print('work2')
        time.sleep(0.2)
        g1.switch()


if __name__ == '__main__':
    # 创建协程指定一个任务
    g1 = greenlet.greenlet(work1)
    # 创建协程指定一个任务
    g2 = greenlet.greenlet(work2)

    g1.switch()
