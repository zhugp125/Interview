#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from io import BytesIO

# write binary data to bytes_io
print('write binary data:')
f = BytesIO()
print(f.write('中国'.encode('utf-8')))
print(f.getvalue())

# read binary data from bytes_io
print('read binary data:')
f = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(f.read())