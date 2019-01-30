#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: baidu.py
@time: 2019/1/25 10:07
'''
import requests
import time
from urllib import request
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1548390013326='

headers = {
'Referer':
'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1548390007766_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E',
'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
}

data_str = '''
tn: resultjson_com
ipn: rj
ct: 201326592
is: 
fp: result
queryWord: 唯美
cl: 2
lm: -1
ie: utf-8
oe: utf-8
adpicid: 
st: -1
z: 
ic: 
hd: 
latest: 
copyright: 
word: 唯美
s: 
se: 
tab: 
width: 
height: 
face: 0
istype: 2
qc: 
nc: 1
fr: 
expermode: 
force: 
pn: 240
rn: 90
gsm: 1e
1548390013326:
'''

send_data = {}
for line in data_str.splitlines():
    line_data = line.split(': ')
    if len(line_data) == 2:
        key,value = line_data
        if key and value:
            send_data[key] = value

response = requests.get(url = url, headers = headers,params=send_data)
content = response.json()['data']

num = 1

for index,src in enumerate(content):
    img_url = src.get('middleURL')
    if img_url:
        name = './image/image_%s_%s.jpg' % ('唯美', index)
        try:
            request.urlretrieve(url=img_url,filename=name)
        except Exception as e:
            print(e)
        else:
            print('%s is down' % name)
