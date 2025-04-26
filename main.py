from twilio.rest import Client
import os
from dotenv import load_dotenv
from gtts import gTTS
import google.generativeai as genai

load_dotenv() 

def whatsapp_chat():

  try:
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
  
  except Exception as e:
    print(f"An error occurred: {e}")



def ai_voice():

  try:
    mytext = response.text
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("technews.mp3")

    # os.system("start welcome.mp3")

  except Exception as e:
    print(f"An error occurred: {e}")
  

def gemini():
    
    global response
    try:
      api_key = os.getenv("GEMINI_API_KEY")
      genai.configure(api_key=api_key)

      model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

      prompt = "Write a 100 word summary of the latest tech news."

      response = model.generate_content(prompt)

      print(response.text)
      return response.text
    except Exception as e:
      print(f"An error occurred: {e}")

      
    

if __name__ == "__main__":
  gemini()
  ai_voice()
  whatsapp_chat()