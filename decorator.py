#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import functools

def fun():
    print('test')

# function has '__name__' attribute
print(fun.__name__) # fun

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kv):
        print('function name: %s()' % func.__name__)
        return func(*args, **kv)
    return wrapper

@log
def now():
    print('2018-4-24')

now() # log(now)
print('__name__ = ', now.__name__)

def log(text = ''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kv):
            print('%s function name: %s()' % (text, func.__name__) )
            return func(*args, **kv)
        return wrapper
    return decorator

@log() #'exec'
def title():
    print('title')

title()
print('__name__ = ', title.__name__)

# test
print('---------test------------')

def call(func):
    @functools.wraps(func)
    def wrapper(*args, **kv):
        print('call begin')
        func(*args, **kv)
        print('call end')
    return wrapper

@call
def hello():
    print('hello world')

hello()
print('__name__ = ', hello.__name__)
