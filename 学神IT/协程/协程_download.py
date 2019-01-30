#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 协程_download.py
@time: 2019/1/30 10:39
'''

import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()

#下载图片函数
def download_image(img_url,img_name):
    try:
        print(img_url)
        # 根据图片地址打开网络进行下载
        response = urllib.request.urlopen(img_url)
        # 把所有数据下载到本地指定的文件名里面
        with open(img_name,'wb') as img_file:
            while True:
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
     # 有异常打印异常
    except Exception as e:
        print('图片下载异常',e)
    # 没有异常打印正常下载
    else:
        print('图片下载成功：%s' % img_name)


if __name__ == '__main__':
    # 准备图片地址
    img_url1 = 'http://p0.so.qhmsg.com/bdr/576__/t013ee81b64eb53f6f5.jpg'
    img_url2 = "http://p2.so.qhimgs1.com/bdr/594__/t017ec94ec006189032.jpg"
    img_url3 = "http://p3.so.qhmsg.com/bdr/864__/t01f9daf42a666bb408.jpg"

    # 开启协程指派相应的任务，第一个参数对应的是一个函数，第二个参数是对应函数的
    g1 = gevent.spawn(download_image,img_url1,'1.jpg')
    g2 = gevent.spawn(download_image, img_url2, '2.jpg')
    g3 = gevent.spawn(download_image, img_url3, '3.jpg')

    # 主线程等待所有的协程执行完成以后程序再退出
    gevent.joinall([g1, g2, g3])
