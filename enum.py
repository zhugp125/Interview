#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

''' python3
Jan => Month.Jan ,  1
Feb => Month.Feb ,  2
Mar => Month.Mar ,  3
Apr => Month.Apr ,  4
May => Month.May ,  5
Jun => Month.Jun ,  6
Jul => Month.Jul ,  7
Aug => Month.Aug ,  8
Sep => Month.Sep ,  9
Oct => Month.Oct ,  10
Nov => Month.Nov ,  11
Dec => Month.Dec ,  12
'''

# 可以直接使用Month.Jan来引用一个常量。value属性则是自动赋给成员的int常量，默认从1开始
for name, member in Month.__members__.items():
    print(name, '=>', member, ', ', member.value)

@unique
class weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以帮助检查保证没有重复值
# 访问这些枚举类型的方法
print(weekday.Mon) # weekday.Mon
print(weekday['Tue']) # Weekday.Tue
print(weekday.Tue.value) # 2
print(weekday.Mon == weekday.Mon) # True
print(weekday.Mon == weekday.Wed) # False
print(weekday(1)) # Weekdat.Monsí