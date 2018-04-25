#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import types

def fn():
    pass

# type
print(type(123)) # <type 'int'>
print(type('str')) # <type 'str'>
print(type(None)) # <type 'NoneType'>

print(type(abs)) # <type 'builtin_function_or_method'>

def fun():
    pass
print(type(fun)) # <type 'function'>

class Animal(object):
    pass

print(type(Animal())) # <type '__main__.Animal'>

# type return value compare
print(type(123) == int)
print(type(123) == type(456))
print(type('123') == str)
print(type(123) == type('123'))
print(type(abs) == types.BuiltinFunctionType)
print(type(fn) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)