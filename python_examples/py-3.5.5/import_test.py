#!/usr/bin/env python
# -*- coding: utf-8 -*-

import temperature_transform as tt

print("32摄氏度 = % .2f华氏度" % tt.c2f(32))
print("99华氏度 = % .2f摄氏度" % tt.f2c(99))


print(__name__)
print(tt.__name__)

