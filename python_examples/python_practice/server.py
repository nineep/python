#!/usr/bin/env python

import socket

host = ''
port = 8088

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((hosts, port))
s.listen(1)

print "server is running on port %d" % port

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write("welcome," + str(clientaddr) + "\n")
    clientfile.write("please enter a string:")
    line = clientfile.readline().strip()
    clientfile.close()
    clientsock.close()
