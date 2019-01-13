#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: rc脚本3-stop和status方法.py
@time: 2019/1/13 2:51 PM

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
    # 进程的pid写入pid文件
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
        print("%s start Sucessful" % self.name)

    # stop时先获取memcached的pid
    def _getPid(self):
        # python2中：p = Popen(['pidof', 'memcached'], stdout=PIPE).stdout.read().strip()
        # 获取memcached进程号
        pid = str(Popen(['pidof', self.name], stdout=PIPE).stdout.read().strip()).split("'")[1]
        return pid


    def stop(self):
        # kill pid以及删除memcached.pid文件
        pid = self._getPid()
        if pid:
            os.kill(int(pid),15)
            if os.path.exists(self._pidFile()):
                os.remove(self._pidFile())
            print("%s is stopped" % self.name)


    def restart(self):
        self.stop()
        self.start()


    def status(self):
        pid = self._getPid()
        if pid:
            print("%s is already running" % self.name)
        else:
            print("%s is not running" % self.name)


    # 如果后面跟的不是start、stop等参数；打印以下说明
    def help(self):
        print("Usage: %s {start|stop|restart|status}" % __file__)


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
    except 'IndexError,e':
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

if __name__ == '__main__':
    main()
