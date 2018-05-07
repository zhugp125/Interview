#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from io import StringIO

# write string io
print('write string to string_io:')
f = StringIO()
print(f.write('hello')) # return write character length
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())     # return write string

# read string io
f = StringIO('Hello!\nHi!\nGoodbye!')
print('read string from string_io:')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())