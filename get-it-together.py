from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv('SID')
auth_token = os.getenv('TOKEN')
to = os.getenv('USER_NUMBER')
sender = os.getenv('TW_NUMBER')


client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to,
    from_=sender,
    body="Testing")

print(message.sid)
