# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText


sender = 'test@mail.com'
receivers = ['nineep@qq.com']

msg = MIMEText('This is the body of a message.', 'plain', 'utf-8')
msg['From'] = Header('测试mail server', 'utf-8')
msg['To'] = Header('测试接受者', 'utf-8')

subject = 'SMTP 邮件测试'
msg['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('127.0.0.1', port=10025)
    smtpObj.set_debuglevel(True)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error: 无法发送邮件')
