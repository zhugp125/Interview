#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from functools import reduce

# map(function, Iterable) -> Iterator
def f(x):
    return x * x

r = map(f, [1, 2, 3 , 4, 5, 6, 7, 8, 9])
print(list(r)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce(function, Iterator)
def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4])
print(r) # 10

# function: string to int
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

ret = reduce(fn, map(char2num, '13579'))
print(ret)
print(isinstance(ret, int))

def title(s):
    return s.title()

names = ['admin', 'LISA', 'HEllo']
names = list(map(title, names))
print(names)

def prod(L):
    def multipy(x, y):
        return x * y

    return reduce(multipy, L)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))

flag = True
base = 10
def str2float(s):
    def fn(x, y):
        global flag, base
        if str(y) == '.':
            flag = False
            base = 1
            return x
        else:
            if flag:
                return x * base + y
            else:
                base = base * 0.1
                return x + y * base

    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':'.'}[s]

    return reduce(fn, map(char2num, s))

print('str2float(\'123.456\')', str2float('123.456'))
