#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

# add attribute to instance by instance or self variable
class Student(object):

    def __init__(self, name):
        self.name = name

st = Student('tom')
st.age = 20
print('name: ', st.name)
print('age : ', st.age)

# class attribute
# each instance for class 'Dog' have class attribute
class Dog(object):
    name = 'dog'

t = Dog()
print('name: ', t.name) # ('name: ', 'dog')

# instance attribute > class attribute
t.name = 'teddy'
print('name: ', t.name) # ('name: ', 'teddy')

# delete instance attribute
del t.name
print('name: ', t.name) # ('name: ', 'dog')