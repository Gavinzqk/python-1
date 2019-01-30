#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: 2. os.walk模块使用.py
@time: 2019/1/28 14:59
'''

import sys,os
import hashlib

def md5sum(f):
    md5 = hashlib.md5()
    with open(f) as fd:
        while True:
            data =fd.read(4096)
            if data:
                md5.update(data)
            else:
                break
    print md5.hexdigest()

m = os.walk(sys.argv[1])
for p,d,f in m:
    print os.path.join(p,f)
