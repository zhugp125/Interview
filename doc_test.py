#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

class Dict(dict):
    '''
    Simple dict but also support access as x.y style

    >>> d = Dict()
    >>> d['x'] = 1
    >>> d.x
    1
    >>> d.y = 2
    >>> d['y']
    2
    >>> d2 = Dict(a=1, b=2, c='a')
    >>> d2.c
    'a'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
    
def fact(n):
    '''
    example function 'fact' test:

    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError: error value: 0
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: error value: -1
    >>> fact('a')
    Traceback (most recent call last):
        ...
    TypeError: 'a' must be integer
    '''
    if not isinstance(n, int):
        raise TypeError("'%s' must be integer" % n)
    if n < 1:
        raise ValueError('error value: %d' % n)
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()