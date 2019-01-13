#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 爬取图片.py
@time: 2019/1/12 5:51 PM

'''

from bs4 import BeautifulSoup
import requests

# 爬取目标网页
html = requests.get("https://tieba.baidu.com/p/5950745302").text

# 解析网页
result = BeautifulSoup(html,'html.parser')

# 获取所有的图片img
result_imgs = result.find_all("img",class_="BDE_Image")


i = 1
for result_img in result_imgs:

    # 获取链接
    img_url = result_img['src']
    # 获取文件
    result_img_content = requests.get(img_url).content
    # 声明文件名
    file_name = './images/' + str(i) + '.jpg'
    # 保存图片
    with open(file_name,'wb') as wf:
        wf.write(result_img_content)

    i += 1


