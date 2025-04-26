from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv() 


account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
print(auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM"),
  content_sid=os.getenv("TWILIO_CONTENT_SID"),
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")
)

print(message.sid)