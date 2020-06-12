# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# qq SMTP server
mail_host = 'smtp.qq.com'
mail_user = 'nineep@qq.com'
mail_pass = '' #在qq邮箱 设置-账户-生成授权码，作为密码

sender = 'nineep@qq.com'
receivers = ['nineep@qq.com']

message = MIMEText('py test mail', 'plain', 'utf-8')
message['From'] = Header('nineep', 'utf-8')
message['To'] = Header('test', 'utf-8')

subject = 'py test mail'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.set_debuglevel(2)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')