#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import hashlib

# md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# call md5.update more

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e', # 123456
    'bob'    : '96e79218965eb72c92a549dd5a330112', # 111111
    'alice'  : '5f4dcc3b5aa765d61d8327deb882cf99'  # password
}

def login(user, password):
    return db[user] == calc_md5(password)

assert login('michael', '123456'), 'user or password error'
assert login('bob', '111111'), 'user or password error'
assert login('alice', 'password'), 'user or password error'