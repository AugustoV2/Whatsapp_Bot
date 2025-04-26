from twilio.rest import Client
import os
from dotenv import load_dotenv
from gtts import gTTS
from google import genai

load_dotenv() 

def whatsapp_chat():
  account_sid = os.getenv("account_sid")
  auth_token = os.getenv("auth_token")
  print(auth_token)
  client = Client(account_sid, auth_token)

  message = client.messages.create(
  from_='whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM"),
  media_url=['F:\vs code\Python\Whatsapp_Bot\technews.mp3'],
  to='whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")
  )

  print(message.sid)


def ai_voice():
  mytext = response.text
  language = 'en'

  myobj = gTTS(text=mytext, lang=language, slow=False)

  myobj.save("technews.mp3")

  # os.system("start welcome.mp3")


def gemini():
 

  client = genai.Client(api_key="YOUR_API_KEY")

  global response

  response = client.models.generate_content(
      model="gemini-2.0-flash", contents="Fetch me the latest 3 tech news",
  )

 
  print(response.text)


if __name__ == "__main__":
  gemini()
  ai_voice()
  whatsapp_chat()