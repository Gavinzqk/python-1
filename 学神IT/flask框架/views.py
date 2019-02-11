#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: views.py
@time: 2019/1/30 15:05
'''

from flask import Flask,render_template

# 创建应用实例
app = Flask(__name__)

#使用装饰器指定路由
@app.route('/index/')

# 路由指向的响应功能
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
    )