#!/usr/bin/env python

'''
Tests to see if the directory testdir exsits,
if not it will create the directory for you.
'''

from __future__ import print_function
import os
import sys

def main():
    if sys.version_info.major >= 3:
        input_func = input
    else:
        input_func = raw_input

    CheckDir = input_func("Enter the name of the directory to check : ")
    print()

    if os.path.exists(CheckDir):
        print("THe directory exists")
    else:
        print("No directory found for " + CheckDir)
        print()
        os.mkdirs(CheckDir)
        print("Directory created for " + CheckDir)

if __name__ == '__main__':
    main()

