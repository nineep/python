import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, 'flaskr.db')

USERNAME = 'admin'
PASSWORD = 'admin'

SECRET_KEY = 'you_never_know'
