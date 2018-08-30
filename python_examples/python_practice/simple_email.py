import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def send_simple_email(warning):
    msg = MIMEText(warning)
    msg['Subject'] = 'python first mail'
    msg['From'] = 'nineep@qq.com'
    try:
        smtp = smtplib.SMTP()
        smtp.connect(r'smtp.qq.com')
        smtp.login('903354120', 'ljy6918057795')
        smtp.sendmail('nineep@qq.com', ['nineep@qq.com'], msg.as_string())
        smtp.close()
    except Exception, e:
        print e

if __name__ == '__main__':
    send_simple_email(warning = "This is a warning")
