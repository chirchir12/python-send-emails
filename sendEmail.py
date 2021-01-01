import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Hooray this is 2021'
msg['From'] = sender_mail
msg['To'] = 'chirchir7370@gmail.com'
msg.set_content('how about dinner today at 5pm')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_mail, password)
    smtp.send_message(msg)
