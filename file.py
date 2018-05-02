#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

# read line
f = open('./TestFile/aaa.txt', 'r')
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
with open('./TestFile/aaa.txt', 'r') as f:
    print(f.read())

# open file read block
# with open('./TestFile/open.png', 'rb') as f:
#    print(f.read())

# with open('./TestFile/bbb.txt', 'r', encoding='utf-8') as f:
#    print(f.read())

# with open('./TestFile/ccc.txt', 'r') as f:
#    print(f.read())

# write file
with open('./TestFile/setting.ini', 'w') as f:
    f.write('[path]')
    f.write('\n')
    f.write('file=/usr/local/include/stdio.h')