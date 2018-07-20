#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, init):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score musqt between 0 ~ 100!')
        self._score = value

