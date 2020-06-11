from ftplib import FTP

ftp = FTP('ftp.debian.org')
ftp.login()

ftp.cwd('debian')
ftp.retrlines('LIST')

with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)

ftp.quit()