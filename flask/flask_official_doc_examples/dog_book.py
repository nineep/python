




# upload file
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/iploads/uploaded_file.txtx')

from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/iploads/' + secure_filename(f.filename))


# cookie
from flask import import request

@app.route('/')
def index():
    username = request.cookies.get('username')

from flask import make_reponse

@app.route('/')
def index():
    resp = male_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

#redirect
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#response
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 4040)
    resp.headers['X-Something'] = 'A value'
    return resp

#session
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



