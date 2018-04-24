#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import functools

f = functools.partial(int, base=2)
print(f('1001'))
print(f('1001', base=10))