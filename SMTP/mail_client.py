# -*- coding: utf-8 -*-

import smtplib
import email.utils
from email.mime.text import MIMEText

# 创建消息
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'nineep@qq.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', port=1025)
server.set_debuglevel(True)  # 显示与服务器的通信

try:
    server.sendmail('author@example.com',
                    ['nineep@qq.com'],
                    msg.as_string())
    print('邮件发送成功')
finally:
    server.quit()
