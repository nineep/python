#!/usr/bin/env python3

def application(environ, start_response):
    start_response('200 OOK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

