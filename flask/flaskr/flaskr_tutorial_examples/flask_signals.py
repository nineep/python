# -*- coding: utf-8 -*-

'''
blinker支持
信号： 发送者通知接受者事情发生， 不鼓励接受者修改数据
信号处理器 乱序执行，不修改任何数据
优势： 安全快速订阅
'''

from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    record = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)



from flask import template_rendered

def captured_templates(app, recorded, **extra):
    def record(sender, template, context):
        recorded.append((template, context))
    return template_renderded.connected_to(record, app)


