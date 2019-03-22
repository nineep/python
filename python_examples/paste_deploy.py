from paste.deploy import loadapp
wsgi_app = loadapp('config:/path/to/config.ini')


#WSGI 应用对象, 可调用
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']


# Setup a Mapper
from routee import Mapper
map = Mapper()
map.connect(None, "/error/{action}/{id}", controller="error")
map.connect("home", "/", controller="main", action="index")

# Match a URL, return a dict or None if no match
result = map.match('/error/myapp/4')



def pipeline_factory(loader, global_conf, **local_conf):
    '''Create a paste pipeline based on the 'auth_startegy' config option.'''
    pipeline = local_conf[cfg.CONF.auth_strategy]
    pipeline = pipeline.split()
    filters = [loader.get_filter(n) for n in pipeline[:-1]]
    app = loader.get_app(pipeline[-1])
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app

