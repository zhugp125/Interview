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
print(type(123) == int) # True
print(type(123) == type(456)) # True
print(type('123') == str) # True
print(type(123) == type('123')) # False
print(type(abs) == types.BuiltinFunctionType) # True
print(type(fn) == types.FunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print(type((x for x in range(10))) == types.GeneratorType) # True

# isinstance(obj, objectName)
class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

# sub object is also a base object
print(isinstance(h, Husky)) # True
print(isinstance(h, Dog)) # True
print(isinstance(h, Animal)) # True

# base object is not a sub object
print(isinstance(d, Husky)) # False

# dir: get all attrtitue or method for a object
print(dir('abc'))

# setattr
# getattr
# hasattrsss