#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender = 'nineep@qq.com'
passwd = 'edhgnqotvjgybgaf'
receiver = 'nineep@qq.com'

def mail():
    ret = True
    try:
        msg = MIMEText('just test', 'plain', 'utf-8')
        msg['From'] = formataddr(['nineep', sender])
        msg['To'] = formataddr(['jiuyang', receiver])
        msg['Subject'] = 'nineep send mail to jiuyang test'

        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, passwd)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
    print('success')
else:
    print('fail')
