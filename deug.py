#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    # assert n != 0, 'n is zero'
    logging.info('n = %d' % n)
    return 10 / n

def main():
    foo('0')

if __name__ == '__main__':
    main()