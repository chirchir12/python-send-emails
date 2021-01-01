import os
import smtplib
import imghdr
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASSWORD')
contactList = ['echirchir@zamara.co.ke', 'chirchir7370@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Hooray this is 2021'
msg['From'] = sender_mail
msg['To'] = ', '.join(contactList)
msg.set_content('we have attachement')
msg.add_alternative("""
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

images = [str(p) for p in Path("./sendemails").glob("*.PNG")]

for image in images:
    with open(image, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_mail, password)
    smtp.send_message(msg)
