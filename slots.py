#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from types import MethodType

class Student(object):
    pass

st = Student()

# add attribute 'name' for 'st' instance
st.name = 'tob'
print(st.name)

def set_age(self, age):
    self.age = age

# add method for instance
st.set_age = MethodType(set_age, st)
st.set_age(25)
print(st.age)

# use __slots__, you can only set some attribute
class Dog(object):
    __slots__ = ('name', 'age')

d = Dog()
d.name = 'dog'
d.age = 1
print(d.name, ': ', d.age)

# d.run = 1