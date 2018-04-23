#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 默认参数会出现的问题
def test_default_param_question(L = []):
    L.append('end')
    return L

print(test_default_param_question()) # end
print(test_default_param_question()) # end end
print(test_default_param_question()) # end end end

def test_default_param(L = None):
    if L is None:
        L = []
    L.append('end')
    return L

print(test_default_param()) # end
print(test_default_param()) # end
print(test_default_param()) # end

# 可变参数
def calc(*numbers):
    sum = 0
    print('length: ', len(numbers))
    for n in numbers:
        sum += n * n

    return sum

print(calc(1, 2, 3))

numbers = [1, 2, 3, 4]
print(calc(*numbers))

# 关键字参数
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

person('xiaoyan', 27)
person('xiaozhu', 26, addr='henan')

# 命名关键字参数
''' python2 is error
def person(name, age, *, city, job):
    print(name, age, city, job)

person('xiaozhu', 26, city='beijing', job='c++')
'''