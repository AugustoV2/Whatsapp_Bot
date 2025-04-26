from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv() 


account_sid = 'AC5d650237c8e3bf97ab2544fcb3916719'
auth_token = os.getenv("auth_token")
print(auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+919645497988'
)

print(message.sid)