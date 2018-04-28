#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# @property: method to attribute

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must is a integer')
        if value < 0 or value > 100 :
            raise ValueError('score must between 0 on 100')

        self.__score = value

st = Student()
st.score = 12
print(st.score)

# a attribute, if define setter and getter, this is a read-write attribute;
# if only define getter, this is a readonly attribute

class Rectangle(object):
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError('width must be integer or float')
        if width <= 0:
            raise ValueError('width must be getter than 0')

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError('height must be integer or float')
        if height <= 0:
            raise ValueError('height must be getter than 0')

        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

r = Rectangle()
r.width = 40
r.height = 30

print(r.width)
print(r.height)
print(r.area) # this is readonly attribute