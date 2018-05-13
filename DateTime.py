#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from datetime import datetime

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2018, 5, 13, 21, 23)
print(dt)

# datetime to timestamp python3
#print(dt.timestamp())

# timestamp to datetime
t = 1526217780
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))