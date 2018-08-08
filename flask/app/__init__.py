from flask_pagedown import PageDown

pagedown = PageDown()

def create_app(config_name):

    pagedown.init_app(app)

