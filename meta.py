#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# type()
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object, ), dict(hello=fn))
h = Hello()
h.hello()

print(type(Hello))
print(type(h))

#''' python3
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

'''
__new__()方法接收到的参数：
1.当前准备创建的类的对象
2.类的名字
3.类继承的父类集合
4.类的方法集合
'''

L = MyList()
L.add(1)
print(L)
#'''