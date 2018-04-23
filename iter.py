#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from collections import Iterable

l = [1, 2, 3, 4]
for v in l:
    print(v)

d = {'a':1, 'b':2, 'c':3}
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

# string object is a iterative object
for ch in 'ABC':
    print(ch)

# is iterative object
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# get index from list : function enumerate
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# use two(or more) variable in for loop
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)