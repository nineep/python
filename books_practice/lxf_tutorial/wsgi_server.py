#!/usr/bin/env python

from wsgiref.simple_server import make_server
from wsgi_hello import application

#创建一个服务器，ip为空，端口8000，处理函数式application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()
