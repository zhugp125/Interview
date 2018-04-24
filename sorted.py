#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# sorted: is a higher order function

numbers = [3, -8, 5, -4, 9]
print(sorted(numbers)) # [-8, -4, 3, 5, 9]

# sort by abs
print(sorted(numbers, key=abs)) # [3, -4, 5, -8, 9]

# string sort
s = ['Zoom', 'tom', 'Abc', 'hebe']

print('string sort')
#default sort
print(sorted(s)) # ['Abc', 'Zoom', 'hebe', 'tom']

# string sort, not case sensitive
print(sorted(s, key=str.lower)) # ['Abc', 'hebe', 'tom', 'Zoom']

# reverse string sort, not case sensitive
print(sorted(s, key=str.lower, reverse=True)) # ['Zoom', 'tom', 'hebe', 'Abc']

# test
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

print(sorted(l, key=by_name)) # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

def by_score(t):
    return t[1]

print(sorted(l, key=by_score)) # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]