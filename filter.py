#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

# filter(function, iterator)
# if function(iter) return True, this iter will insert to ret

def is_even_number(n):
    return n % 2 == 0

print(filter(is_even_number, range(1, 11)))

def not_empty(s):
    return s and s.strip()

l = ['a', '', 'b', 'c', '  ', ' d']
print(filter(not_empty, l))

#''' python3
print('get prime number')
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    iter = _odd_iter()
    while True:
        n = next(iter)
        yield n
        iter = filter(_not_divisible(n), iter)
        print(iter)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#'''

def is_palindrome(n):
    s = str(n)
    beg, end = 0, -1
    while beg < len(s) / 2:
        if s[beg] != s[end]:
            return False
        beg = beg + 1
        end = end - 1
    return True

print(filter(is_palindrome, range(1, 1000)))