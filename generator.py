#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# generator
g = (x * x for x in range(11))

print(next(g))

for n in g:
    print(n)

# function object
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

    return 'None'

fib(6)

# make generator from function object
def g_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print('***********************************')
gf = g_fib(6)
for n in gf:
    print(n)

# execution sequence for generator
def odd():
    print('step 1')
    yield 1
    print('step 3')
    yield 3
    print('step 5')
    yield 5

o = odd()
for n in o:
    print(n)

# 杨辉三角
def triangles():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i - 1] + l[i] for i in range(len(l))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break