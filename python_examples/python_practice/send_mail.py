import smtplib
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com", "25")
smtp.login('账号', '密码')
origHdrs = ['From:nineep@qq.com', 'To:nineep@foxmail.com', 'Subject: test msg']
origBody = ["This is by python send mail demo!"]
smtp.sendmail('nineep@qq.com', 'nineep@foxmail.com',
              "\r\n\r\n".join(["\r\n"join(origHdrs), "\r\n".join(origBody)]))
smtp.quit()
