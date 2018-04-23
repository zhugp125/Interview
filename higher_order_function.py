#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# general function
def f(a):
    assert(a != 0)
    if a >= 0:
        return a
    else:
        return -a

def g(x, y, f):
    assert(x != 0)
    assert(y != 0)
    return f(x) + f(y)

print(g(-2, 3.0, f))