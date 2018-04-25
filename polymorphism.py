#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# inherit
class Animal(object):

    def run(self):
        print('animal is running')

class Dog(Animal):

    def run(self):
        print('dog is running')

class Cat(Animal):
    
    def run(self):
        print('cat is running')

a = Animal()
d = Dog()
c = Cat()

# polymorphism: different objects respond differently to the same message
a.run()
d.run()
c.run()

def run_twice(a):
    a.run()

run_twice(d)
run_twice(c)
run_twice(a)

class flower(object):

    def run(self):
        print('flower')

run_twice(flower())