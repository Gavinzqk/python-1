#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 协程_360图片下载.py
@time: 2019/1/30 11:53
'''

import gevent
from gevent import monkey
monkey.patch_all()
import requests
from urllib import request



def download_img(num):
    print('start download')
    url = 'http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1'
    headers = {
        'Referer': 'http://image.so.com/z?ch=beauty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    str_data = '''ch: beauty
    sn: 120
    listtype: new
    temp: 1
    '''
    send_data = {}
    for data in str_data.splitlines():
        line_data = data.split(': ')
    if len(line_data) == 2:
        key, value = line_data
        if key and value:
            send_data[key] = value
    send_data['sn'] = eval(str(num)+'*'+'30')
    response = requests.get(url, headers=headers, params=send_data)
    json_data = response.json()['list']
    for index, src in enumerate(json_data):
        image_url = src['qhimg_url']
        try:
            image_name = './360_image/' + image_url[-8:]
            request.urlretrieve(url=image_url, filename=image_name)
        except Exception as e:
            print(e)
        else:
            print('{} is download'.format(image_name))
    print('image is download')
if __name__ == '__main__':
    num = int(input('请输入你想要的组:'))
    # gevent_list = []
    # for i in range(1,num+1):
    #     gevent_list.append(gevent.spawn(download_img,i))
    gevent.joinall([gevent.spawn(download_img,i) for i in range(1,num+1)])
