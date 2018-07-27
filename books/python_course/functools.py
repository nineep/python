#!/usr/bin/env python

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*srgs, **kw):
                print 'call %s():' % func.__name__
                return func(*args, **kw)
            return wrapper

import functools

def log(tesx):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
