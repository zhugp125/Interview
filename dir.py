#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os

# os name
# posix: Linux, Unix, Mac OS x
# nt: windows
print(os.name)

# os info
# 'os' object has no attribute 'uname' in windows
print(os.uname())

# os environment
print(os.environ)
print(os.environ.get('USER'))
print(os.environ.get('U', 'default'))

# print current absoulte path
print(os.path.abspath('.'))

# make dir
dir_name = os.path.join('.', 'testdir')
os.mkdir(dir_name)

# delete dir
os.rmdir(dir_name)

dir_name = '/Users/a123/Downloads/Github/Interview/dir.py'
# split dir
print(os.path.split(dir_name))    # (/Users/a123/Downloads/Github/Interview, dir.py)
print(os.path.splitext(dir_name)) # (/Users/a123/Downloads/Github/Interview/dir, .py)

# rename: file is exists
os.rename('./TestFile/text.txt', 'text.py')

# delete name: file is exists
os.remove('./text.py')

# filter file
print([x for x in os.listdir('.') if os.path.isdir(x)])

# .py file list
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# opeartor dor or file module
# os, os.path, shutil