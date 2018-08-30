#!/usr/bin/env python
number = 7
guess = -1
print('number guess')
while guess != number:
    guess = int(input('input: '))
    
    if guess == number:
        print('right')
    elif guess < number:
        print('low')
    elif guess > number:
        print('high')


