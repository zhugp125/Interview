#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# __str__
class Student(object):

    def __init__(self, name):
        self.__name = name

    # __str__() return string for user
    def __str__(self):
        return 'student object (name: %s)' % self.__name
    
    # __repr__() return string for debug
    __repr__ = __str__

st = Student('Tom')
print(st)

''' python3
# __iter__
class Fib(object):

    def __init__(self, beg, end):
        self.__a = 0
        self.__b = 1
        self.__beg = beg
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__beg >= self.__end:
            raise StopIteration()
        
        self.__beg = self.__beg + 1
        self.__a, self.__b = self.__b, self.__a + self.__b
        return self.__a

for n in Fib(0, 8):
    print(n)
'''

# __getitem__(), __setitem__(), __delitem__()
class StudentRank(object):
    
    def __init__(self):
        self.__rank = {}

    def __setitem__(self, student, rank):
        print('set item: (student: %s, rank: %s)' % (student, rank))
        self.__rank[student] = rank

    def __delitem__(self, student):
        print('del item: (student: %s)' % student)
        del self.__rank[student]

    def __getitem__(self, student):
        print('get item: (student: %s)' % student)
        return self.__rank[student]

sr = StudentRank()
sr['tom'] = 1
sr['Hebe'] = 2

print(sr['Hebe'])

del sr['Hebe']
# print(sr['Hebe']) # KeyError

# print(help(slice))

# slice
class Slice(object):
    
    def __getitem__(self, n):
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            print(step)
            if start is None:
                start = 0
            if step is None:
                step = 1
            L = []
            i = 0
            for v in range(start, stop):
                if i % step == 0:
                    L.append(v)
                i = i + 1
            return L

s = Slice()
print(s[:8:2])

# __getattr__()
class MiddleStudent(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __getattr__(self, attr):
        if attr == 'score':
            return 80
        elif attr == 'age':
            return lambda: 24
        return AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

ms = MiddleStudent('Team')
print(ms.name)
print(ms.score)
print(ms.age())

# __call__
class Callable(object):

    def __init__(self, name):
        self.__name = name

    def __call__(self, age):
        if not isinstance(age, int):
            raise TypeError('age is must be integer type')
        print('My name is %s, %d old' % (self.__name, age))

c = Callable('Tom')
c(24)