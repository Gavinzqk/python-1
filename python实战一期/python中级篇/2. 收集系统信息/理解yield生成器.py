#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 理解yield生成器.py
@time: 2019/1/31 12:23
'''

# a = (x for x in range(5))
# print(next(a))
# print('*'*30)
# for i in a:
#     print(i)


# 生成器函数直接调用返回的是一个生成器对象，需要实例化后for循环调用
# def h():
#     print('one')
#     yield 1
#     print('two')
#     yield 2
#     print('three')
#     yield 3
# a = h()
# for i in a:
#     print(i)




# def f(n):
#     for i in range(n):
#         yield i
# a = f(3)
# for x in a:
#     print(x)


import hashlib,sys,os
def md5sum(f):
    with open(f,encoding='UTF-8') as fd:
        md5 = hashlib.md5()
        while True:
            data = fd.read(4096)
            if data:
                md5.update(data.encode('utf-8'))  # 注意转码
            else:
                break
        print(md5.hexdigest())

def file_md5(topdir):
    a = os.walk('.')
    for p,d,f in a:
        for i in f:
            file = os.path.join(p,i)
            m = md5sum(file)
            yield '%s  %s' % (m,file)

if __name__ == '__main__':
    try:
        topdir = sys.argv[1]
    except:
        print('%s follow a dir' % __file__ )
        sys.exit()
    gen = file_md5(topdir)
    for i in gen:
        print(i)













