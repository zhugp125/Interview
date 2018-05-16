#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections import namedtuple

# use namedtuple to create a point object
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# create a circle object
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
from collections import deque

d = deque(['a', 'b', 'd']) # d ['a', 'b', 'c']
print(d)
d.append('d')              # d ['a', 'b', 'c', 'd']
print(d)
d.appendleft('f')          # d ['f', a', 'b', 'c', 'd']
print(d)
d.pop()                    # d ['f', a', 'b', 'c']
print(d)
d.popleft()                # d ['a', 'b', 'c']
print(d)

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'default')
dd['key1'] = 123
print(dd['key1']) # 123
print(dd['key2']) # default

# OrderedDict
from collections import OrderedDict

print(dict([('a', 1), ('b', 2), ('c', 3)]))        # {'a': 1, 'c': 3, 'b': 2}
print(OrderedDict([('a', 1), ('b', 2), ('c', 3)])) # {'a': 1, 'b': 2, 'c': 3}

# Counter
from collections import Counter

c = Counter()
for ch in 'booking':
    c[ch] = c[ch] + 1

print(c) # {'o': 2, 'b': 1, 'g': 1, 'i': 1, 'k': 1, 'n': 1}