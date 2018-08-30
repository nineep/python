#!/usr/bin/env python

from warnings import warn

class ReqStrSugRepr(type):

    def __init__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(
            name, bases, attrd)
        
        if '__str_' not in attrd:
            raise TypeError(
                "Class requires overriding of __str__()")

        if '__repr__' not in attrd:
            warn(
                'Class suggests overriding of __repr__()\n', stacklevel=3)
