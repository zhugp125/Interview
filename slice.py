#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
slice [[beg=0]:[end=npos]:[step=1]]
'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[0:3]) # 1, 2, 3
print(L[:3])  # 1, 2, 3
print(L[6:9]) # 7, 8, 9
print(L[6:])  # 7, 8, 9
print(L[-3:]) # 7, 8, 9
print(L[0:5:2]) # 1, 3, 5
print(L[::2]) # 1, 3, 5, 7, 9
print(L[::])  # 1, 2, 3, 4, 5, 6, 7, 8, 9