#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time, threading

# thread will excute this code
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended...' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join() # main thread die after loop thread
print('thread %s is ended...' % threading.current_thread().name)