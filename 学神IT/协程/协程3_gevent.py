#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 协程3_gevent.py
@time: 2019/1/30 10:25
'''

#
# import gevent
#
# def work(n):
#     for i  in range(n):
#         print(gevent.getcurrent(),i)
#         gevent.sleep(1)
#
# g1 = gevent.spawn(work,5)
# g2 = gevent.spawn(work,5)
# g3 = gevent.spawn(work,5)
# g1.join()
# g2.join()
# g3.join()




import gevent,time
from gevent import monkey

# 打补丁，让咱们的gevent识别好时代操作，time.sleep网络请求延迟
monkey.patch_all()

def work1(num):
    print('work1')
    time.sleep(0.2)

def work2(num):
    for i in range(num):
        print('work2')
        time.sleep(0.2)

if __name__ == '__main__':
    g1 = gevent.spawn(work1,3)
    g2 = gevent.spawn(work2,3)
    g1.join()
    g2.join()
