#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

# read line
f = open('./TestFile/aaa.txt', 'r', encoding='gbk')
files = f.readlines()
for file in files:
    print(file.strip())
f.close()

# try open not exists file
try:
    f = open('./TestFile/ddd.txt', 'r')
except IOError as e:
    print('except:', e)
finally:
    f.close()

# open file readonly
with open('./TestFile/aaa.txt', 'r', encoding='gbk') as f:
    print(f.read())

# open file read block
with open('./TestFile/open.png', 'rb') as f:
    print(f.read())

#default encoding is utf-8
with open('./TestFile/bbb.txt', 'r') as f:
    print(f.read())

with open('./TestFile/ccc.txt', 'r') as f:
    try:
        print(f.read())
    except UnicodeDecodeError as e:
        print('except:', e)    

# write file
with open('./TestFile/setting.ini', 'w') as f:
    f.write('[path]')
    f.write('\n')
    f.write('file=/usr/local/include/stdio.h')

# python2
# open(name[, mode[, buffering]]) -> file object
# python3
# open(file, mode='r', buffering=-1, encoding=None, newline=None, closefd=True, opener=None)
# Open file and return a stream. Raise IOError upon failure