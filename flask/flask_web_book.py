
context:
#上下文
#类似一个 临时的中间介质， 承接上文和下文直接的变量传递，但是push之后就会pop掉，只是临时起作用
#这个中间商使得url请求和url视图函数之间 简洁灵活
current_app
g
request
session

request_hooks:
#在视图函数前后执行的一些操作，增加灵活性
before_first_request
before_request
after_request
teardown_request
#在请求钩子函数和视图函数之间 共享数据 一般使用上下文全局变量g
#before_request 处理程序可以从数据库中加载已登录用户，并将其保存到g.user中
#随后调用视图函数，视图函数再使用g.user获取用户

#响应
#Flask调用是视图函数后，将其返回值作为响应内容（字符串 + 状态码）
#改变状态码
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400
#设置cookie
from flask import mae_response
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
#重定向
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')
#处理错误
from flask import abort
@app.route('/usr/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

#Flask extension
flask_script #扩展命令行参数

#模板template
user register -> add name to form -> submit -> flask route -> 视图函数处理 -> request_db and add user -> generate response html -> user
模板是一个包含响应文本的 文件， 其中包含 用占位变量表示的动态部分， 其具体值只在请求的上下文context中才能知道
使用真实值替换文件中的变量，再返回最终得到的响应字符串，这个过程叫做渲染，其实就是传入参数到模板，然后得到结果
#jinja2
<h1>Hello, {{ name }}!</h1>   #ansible的template模块也用jinja2
#template render：模板渲染
render_template 方法
#变量 variables
#变量过滤器
safe
capitalize
lower
upper
title
trim
striptags
#控制结构
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}

<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
#宏，类似python中的函数
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>
#重复使用宏
{% import 'macros.html' as macros %}
<ul>
    {% for comment in comments %}
        {{ macros.render_comment(conment) }}
    {% endfor %}
</ul>
#reuse template
{% include 'common.html' %}
#模板继承
cat base.html
<html>
<head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblkck %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>

cat extend.html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style>
    </style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}
#flask-bootsrap: Twitter 的前端模板bootsrap



