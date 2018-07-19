#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'M L'

'''
Database operation module.
'''

import time, uuid, functools, threading, logging

# Dict object:

class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

def next_id(t=None):
    if t is None:
        t = time.time()
    return '


