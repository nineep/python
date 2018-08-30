from wsgiref.simple_server import make_server

def application(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        response_body = "Index"
    else:
        response_body = "Hello"
    status = "200 OK"
    response_headers = [("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

httpd = make_server(
    '127.0.0.1', 8051, application)

httpd.server_forever()


def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

class Upperware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response):
        for data in self.wrapped_app(environ, start_response):
            return data.upper()

from wsgiref.simple_server import make_server

application = Upperware(simple_app)
httpd = male_server('127.0.0.1', 8051, application)
httpd = make_server('127.0.0.1', 8051, application)
httpd.serve_forever()


