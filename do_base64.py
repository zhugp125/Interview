#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import base64

s = base64.b64encode(b'Hello World')
print(s)

s1 = base64.b64decode(s)
print(s1)

print('----------------------------')

s = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)

url_s = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(url_s)

url_r = base64.urlsafe_b64decode('abcd--__')
print(url_r)