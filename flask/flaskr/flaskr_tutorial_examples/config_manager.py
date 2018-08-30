

from flask import Flask

app = Flask(__name__)

app.config['TESTING'] = True
app.testing = True

app.config.update(
    TESTING=True,
    SECRET_KEY=b'dadeded'
)


FLASK_ENV

#常用内置配置变量
#配置文件本身实质是 Python 文件。只有全部是大写字母的变量才会被配置对象所使 用。因此请确保使用大写字母。
ENV
DEBUG
TESTING
SECRET_KEY
SESSION_COOKIE_NAME
SERVER_NAME
APPLICATION_ROOT


# 1 从配置文件中 设置配置
# 2 从环境变量中 设置配置

#使用配置文件
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
#shell 中执行
export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
python run-app.py

#使用环境变量
export SECRET_KEY='5f352379324c22463451387a0aec5d2f'
export DEBUG=False
python run-app.py

import os
ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default=False)
if ENVIRONMENT_DEBUG.lower() in ("f", "false"):
    ENVIRONMENT_DEBUG = False

DEBUG = ENVIRONMENT_DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
if not SECRET_KEY:
    rasie ValueError('No secret key set for Flask application")

