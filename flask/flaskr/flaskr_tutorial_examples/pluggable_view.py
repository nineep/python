
@app.route('/users/')
def show_users(page):
    users = User.query.all()
    return render_template('users.html', users=users)

from flask.views import View
class ShowUsers(View):
    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))


from flask.views import MethodView

class UserAPI(MethodView):
    def get(self):
        users = User.query.all()
        ...and

    def post(self):
        user = User.from_form_data(request.form)
        ...and

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))


# decorate view
def user_required(f):
    '''
    Check whether user is logged in or raises error 401.
    '''
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/users/', view_func=view)

# API methodview

class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            # 返回一个包含所有用户的列表
            pass
        else:
            # 显示一个用户
            pass

    def post(self):
        # 创建一个用户
        pass

    def delete(self, user_id):
        #删除用户
        pass

    def put(self, user_id):
        # 更新用户
        pass

user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, default={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

register_api(UserAPI, 'user_api', '/users/', pk='user_id')


    def post(self)
