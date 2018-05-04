#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pickle
import json

# pickle: python serialization

d = dict(a='1', b=2, c='hebe')
pRet = pickle.dumps(d)

print(pickle.loads(pRet))

# pickle to file
with open('pickle.txt', 'wb') as f:
    pickle.dump(d, f)

with open('pickle.txt', 'rb') as f:
    print(pickle.load(f))

# json: common serialization
jRet = json.dumps(d)

print(json.loads(jRet))

# json to file
with open('json.txt', 'wb') as f:
    json.dump(d, f)

with open('json.txt', 'rb') as f:
    print(json.load(f))

# custom class
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def studentToDict(st):
    return dict(name=st.name, age=st.age, score=st.score)

def toStudent(s):
    return Student(s['name'], s['age'], s['score'])

st = Student('Tom', 18, 81)
ret = json.dumps(st, default=lambda obj: obj.__dict__) # default=studentToDict
print(ret)
print(json.loads(ret, object_hook=toStudent))