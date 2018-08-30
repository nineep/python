#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask import render_template
<<<<<<< HEAD:flask/hello_flask_bootsrap.py
from flask.ext.bootstrap import Bootstrap
=======
from flask_bootstrap import Bootstrap
>>>>>>> 12117a7a1f4b10c67a878a987ef14030183ec3e0:flask/flasky_examples/hello_flask_bootsrap.py


app = Flask(__name__)
manager = Manager(app)
bootsrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()
