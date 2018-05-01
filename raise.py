#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# raise error
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

#foo('0')

print('\n')
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
