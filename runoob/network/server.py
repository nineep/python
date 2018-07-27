#!/usr/bin/env python3

import socket
import sys

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

while True:
    cs,addr = ss.accept()
    print('connection addr: %s' % str(addr))

    msg = 'welcome!' + '\r\n'
    cs.send(msg.encode('utf-8'))
    cs.close()
