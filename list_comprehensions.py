#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

'''
list comprehensions
[element for value in range [if] ]
'''

print(range(1, 11)) # 1, 2, ..., 10
print([x for x in range(1, 11)]) # 1, 2, ..., 10
print([x for x in range(1, 11) if x % 2 == 0]) # 2, 4, 6, 8, 10
print([x * x for x in range(1, 11)]) # 1 * 1, 2 * 2, 3 * 3, ..., 10 * 10

print([m + n for m in 'abc' for n in '123']) # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

d = {'a':1, 'b':2, 'c':3}
print([k + '=' + str(v) for k, v in d.items()]) # ['a=1', 'c=3', 'b=2']

# string to lower
L = ['Baidu', 'AliBaBa', 'Tencent']
print([s.lower() for s in L]) # ['baidu', 'alibaba', 'tencent']

L = ['Baidu', 'AliBaBa', 'Tencent', 123]
print([s.lower() for s in L if isinstance(s, str)]) # ['baidu', 'alibaba', 'tencent']
