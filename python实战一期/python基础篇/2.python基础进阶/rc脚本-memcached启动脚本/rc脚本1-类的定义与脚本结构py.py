#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: rc脚本.py
@time: 2019/1/12 5:36 PM

'''
import sys,os

class Process(object):
    '''memcached rc script'''

    def __init__(self,name,program,args,workdir):
        self.name = name
        self.program = program
        self.args = args
        self.workdir = workdir


    def _init(self):


    def start(self):


    def stop(self):


    def restart(self):
        self.stop()
        self.start()


    def status(self):


    def help(self):




def main():
    name = 'memcached'
    prog = '/usr/bin/memcached'
    args = '-u nobody -p 11211 -c 1024 -m 64'
    wd = '/var/tmp/memcached'


    pm = Process(name = name,
                 program = prog,
                 args = args,
                 workdir = wd)

    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print('Option error')
        sys.exit()
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        pm.help()

if __name__ = '__main__':
    main()