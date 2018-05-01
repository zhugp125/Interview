#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import logging

# try-catch

def division(x, y):
    return int(x) / int(y)

print('try...catch')
try:
    print('result:', division(10, 'a'))
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('end\n')

# error debug
def double(x, y):
    return division(x, y) * 2

def main():
    try:
        double(10, '0')
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()

