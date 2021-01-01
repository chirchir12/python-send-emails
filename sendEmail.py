import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # ecrypt
    smtp.ehlo()

    smtp.login(sender_mail, password)
    subject = 'Hello there!!!!!!!!'
    body = 'this is your first email man'

    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(sender_mail, 'chirchir7370@gmail.com', msg)
