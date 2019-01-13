#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: rc脚本-步骤2-start方法.py
@time: 2019/1/13 11:14 AM

'''

import sys
import os
from subprocess import Popen,PIPE

class Process(object):
    '''memcached rc script'''

    def __init__(self,name,program,args,workdir):
        self.name = name
        self.program = program
        self.args = args
        self.workdir = workdir


    def _init(self):
        '''pid目录 /var/tmp/memcached'''

        # 判断目录不存在的话创建并进入workdir目录
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)

    # 声明pid文件名
    def _pidFile(self):
        ''' /var/tmp/memcached/memcached.pid '''
        return os.path.join(self.workdir,"%s.pid" % self.name)

    def _writePid(self):
        if self.pid:
            with open(self._pidFile(), 'w') as fd:
                fd.write(str(self.pid))

    def start(self):
        self._init()
        cmd = self.program + ' ' + self.args
        # shell 中执行命令需要导入Popen和PIPE模块
        p = Popen(cmd, stdout=PIPE, shell=True)
        self.pid = p.pid
        self._writePid()
        print("$s start Sucessful" % self.name)




    def stop(self):
        pass


    def restart(self):
        self.stop()
        self.start()


    def status(self):
        pass



    def help(self):
        pass




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