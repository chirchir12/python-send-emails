import os
import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Hooray this is 2021'
msg['From'] = sender_mail
msg['To'] = 'chirchir7370@gmail.com'
msg.set_content('we have attachement')

with open('sendemails/image1.PNG', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_mail, password)
    smtp.send_message(msg)
