#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from multiprocessing import Process
import os

# child process excute code
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('child', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')