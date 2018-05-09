#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import pathlib # only import by python3

# 1. get the upper directory
print('------------* os.path *--------------')
pwd = os.getcwd()
print('current directory:', pwd)

father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+'.')
print('upper directory:', father_path)

grandfather_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+'..')
print('upper-upper directory:', grandfather_path)

print('------------* pathlib *--------------')
pwd = pathlib.Path.cwd()
print('current directory:', pwd)
print('upper directory:', pwd.parent)
print('upper-upper directory:', pwd.parent.parent)

# 2. usr directory / current directory
print('------------* os.path *--------------')
print('home:', os.environ['HOME'])
print('home:', os.path.expandvars('$HOME'))
print('cwd:', os.getcwd())
print('home:', os.path.expanduser('~'))

print('------------* pathlib *--------------')
print('home:', pathlib.Path.home())
print('cwd:', pathlib.Path.cwd())

# 3. get make dir path
print('------------* os.path *--------------')
cwd = os.getcwd()
print(cwd+os.path.sep+'my.conf')

print('------------* pathlib *--------------')
cwd = pathlib.Path.cwd()
print(cwd / 'my.conf')
print(cwd.joinpath('my.conf'))

print('file name:', cwd.name)
print('suffix:', cwd.suffix)
print('anchor:', cwd.anchor)
print('root:', cwd.root)
print('parts:', cwd._parts)

# 4. file operator
print('------------* pathlib *--------------')
cwd = pathlib.Path.cwd()
file_path = cwd / 'my.conf'
file_path.write_text('debug = 1\ntext')

with file_path.open(mode='r') as f:
    for line in f:
        print(line)
print(file_path.read_text())

# 5. rename / modify suffex
file_path.replace(file_path.with_name('your.conf'))

file_path = cwd / 'your.conf'
file_path.replace(file_path.with_suffix('.conf'))