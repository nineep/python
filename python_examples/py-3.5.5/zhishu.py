#!/usr/bin/env python3

#定义除数
for n in range(2, 10):
    #定义被除数，1-除数之间的所有数
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, ' 是质数')
