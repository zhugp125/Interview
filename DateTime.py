#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2018, 5, 13, 21, 23)
print(dt)

# datetime to timestamp python3
print(dt.timestamp())

# timestamp to datetime
t = 1526217780
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# string to datetime
print(datetime.strptime('2018-5-15 22:43:30', '%Y-%m-%d %H:%M:%S'))

# datetime to string
print(datetime.now().strftime('%a, %b %d %H:%M'))

# use class 'timedelta' to time calculate
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))

# test : string to timestamp
def to_timestamp(dt_str, tz_str):
    t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    obj = re.match(r'UTC([+-])([0-9]{1,2}):00', tz_str)
    if obj:
        c = obj.group(1)
        d = obj.group(2)

    if c == '+':
        tz_utc = timezone(timedelta(hours=int(d)))
    elif c == '-':
        tz_utc = timezone(timedelta(hours=int(d) * -1))
    else:
        tz_utc = None
    t = t.replace(tzinfo=tz_utc)
    return t.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
