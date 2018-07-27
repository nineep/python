#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

source = ['/home/test/']
target_dir = '/home/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Sucessful backup'
else:
    print 'Backup Failed'
