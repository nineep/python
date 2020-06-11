import smtplib
from smtplib import SMTP

s = SMTP('localhost', port=8025)
try:
    s.set_debuglevel(True)
    s.sendmail('andy@love.com', ['bob@hate.com'], """\
    Date:17/05/2017,2:18
    From: andy@love.com
    To: nineep@qq.com
    Subject: A test
    testing
    """)
    s.quit()
except smtplib.SMTPException:
    print("Error: unable to send email")
    import traceback
    traceback.print_exc()