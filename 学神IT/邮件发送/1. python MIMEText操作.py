#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 1. python MIMEText操作.py
@time: 2019/1/23 12:12
'''
# xePTpx3YNaACQfru

import smtplib #构建发送规定服务器模块
from email.mime.text import MIMEText #发送的文本内容
# 构造发送者和接收者，pop3的数千码
from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
# 构造发送的信息
msg = MIMEText('hello,honeyhong')
#腾讯对公接口
smtp_server= 'smtp.qiye.163.com'
#构建自己的发送服务器
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(from_addr,password)
# 发送邮件，第一个参数发送者，第二个参数接收者，第三个参数发送的信息
server.sendmail(from_addr,to_addr,msg.as_string())

server.close()