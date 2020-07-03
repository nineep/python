# -*- coding: utf-8 -*-
import subprocess

subprocess.getoutput('ipconfig')
a=subprocess.check_output('ipconfig', stderr=subprocess.STDOUT)
print(a)