import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_mail, password)
    subject = 'Hello there!!!!!!!!'
    body = 'this is your first email man'

    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(sender_mail, 'chirchir7370@gmail.com', msg)
