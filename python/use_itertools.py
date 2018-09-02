#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import itertools

# 三个无限迭代器
natutals = itertools.count(start=1, step=2)
for n in natutals:
    if n < 15:
        print(n)
    else:
        break

cs = itertools.cycle('abc')
count = 0
for c in cs:
    if count < 4:
        print(c, )
        count += count + 1
    else:
        break

# 第二个参数表示次数，默认无限次
ns = itertools.repeat('a', 4)
for n in ns:
    print(n, )

# 从无限迭代中取有限次数
natutals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natutals)
for n in ns:
    print(n, )

# chain()
for c in itertools.chain('abc', 'xyz', 'chain'):
    print(c, )

# groupby() 分组
for key, group in itertools.groupby('aaabbbddeeggg'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBddbEeff', lambda c : c.lower()):
    print(key, list(group))