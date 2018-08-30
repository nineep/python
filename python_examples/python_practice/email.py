from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib
import datetime

msg = MIMEMultipart()
att = MIMEText(open('test.xlsx', 'rb').read(), 'base64', 'gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="test.xlsx"'
msg.attach(att)

msg['to'] = 'nineep@qq.com'
msg['from'] = 'nineep@qq.com'
msg['subject'] = Header('ceshijieguo('+ str(datetime.today()) + ')', 'gb2312')

server = smtplib.SMTP()
server.login("user", "passwd")
server.sendmail(msg['from'], msg['to'], msg.as_string())
server.close
