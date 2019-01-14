#! /usr/bin/env python
# encoding: utf-8
'''
@author:Gavin
@contact: zqkaiyu@163.com
@file: rc脚本4-daemon启动.py
@time: 2019/1/13 2:51 PM

'''

'''
以daemon方式运行时加了参数 -d 和-P; -P只能和-d一起使用，指定写入pid的pid文件
args参数需要重新设定，参数和/etc/sysconfig/memcached文件里冲突时，调用/etc/sysconfig/memcached文件里参数。
修改/etc/sysconfig/memcached时，下次启动参数会跟着变
'''




import sys
import os
from subprocess import Popen,PIPE

class Process(object):
    '''memcached rc script'''
    # 定义args公有属性
    args = {'USER':'memcached',
            'PORT':11211,
            'MAXCONN':1024,
            'CACHESIZE':64,
            'OPTIONS':''}


    def __init__(self,name,program,workdir):
        self.name = name
        self.program = program
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

    # 读/etc/sysconfig/memcached文件，并返回一个字典
    def _readConf(self,f):
        with open(f) as fd:
            lines = fd.readlines()
            return dict([i.strip().replace('"','').split('=') for i in lines])

    # 解析参数调用_readConf方法,如果对应的参数key在memcached文件中则把value替换到参数中
    def parseArgs(self):
        conf = self._readConf('/etc/sysconfig/memcached')
        if 'USER' in conf:
            self.args['USER'] = conf['USER']
        if 'PORT' in conf:
            self.args['PORT'] = conf['PORT']
        if 'MAXCONN' in conf:
            self.args["MAXCONN"] = conf["MAXCONN"]
        if 'CACHESIZE' in conf:
            self.args["CACHESIZE"] = conf["CACHESIZE"]

        options = ['-u', self.args["USER"],
                   '-p', self.args['PORT'],
                   '-m', self.args['CACHESIZE'],
                   '-c', self.args['MAXCONN']]

        # 把/var/tmp/memcached 目录的所有者改成memcached启动用户
        os.system('chown %s %s' % (self.args['USER'],self.workdir))
        return options


    def start(self):
        # 已经启动memcached时在启动start会影响pid文件里写入当pid值，所以start时先判断是否启动了memcached
        pid = self._getPid()
        if pid:
            print('%s is running...' % self.name)
            sys.exit()

        self._init()
        #cmd改成列表格式
        cmd = [self.program] +  self.parseArgs() + ['-d', '-P',self._pidFile()]

        # shell 中执行命令需要导入Popen和PIPE模块，cmd为列表时shell为默认的false不用指定
        p = Popen(cmd, stdout=PIPE)

        # -P会写入pid到pid文件，下面两行不用调用
        # self.pid = p.pid
        # self._writePid()
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
    wd = '/var/tmp/memcached'


    pm = Process(name = name,
                 program = prog,
                 workdir = wd)

    try:
        cmd = sys.argv[1]
    except:
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
