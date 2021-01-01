# python3 -m smtpd -c DebuggingServer -n localhost:1025
import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')


with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'Hello there!!!!!!!!'
    body = 'this is your first email man'

    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(sender_mail, 'chirchir7370@gmail.com', msg)
