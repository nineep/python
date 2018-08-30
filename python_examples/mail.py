#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'nineep@qq.com'
receivers = ['nineep@qq.com']

message = MIMEText('Mail test', 'plain', 'utf-8')
message['From'] = Header("sender", 'utf-8')
message['To'] = Header("receivers", 'utf-8')

subject = 'Python mail test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("send mail successfuly")
except smtplib.SMTPException:
    print("Error: send mail fail")
