import os
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.environ.get('MY_EMAIL')
passord = os.environ.get('EMAIL_PASSWORD')
print(passord)
