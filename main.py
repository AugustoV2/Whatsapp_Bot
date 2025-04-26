from twilio.rest import Client
import os
from dotenv import load_dotenv
from gtts import gTTS
import requests
import google.generativeai as genai

load_dotenv() 
# Removed global temp_link as it is no longer needed

def whatsapp_chat(temp_link):

  try:
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    print(auth_token)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM"),
    body='Here is an audio file for you!',
    media_url=[temp_link],
  
    to='whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")
    )

    print(message.sid)
  
  except Exception as e:
    print(f"An error occurred: {e}")


def upload_audio_temp(file_path):
  global audio_url
 
  try:

  
    with open("technews.mp3", 'rb') as file:
      audio_url = requests.post('https://file.io', files={'file': file})

    if audio_url.status_code == 200:
      temp_link = audio_url.json().get('link')
      print(f"File uploaded successfully: {temp_link}")
      return temp_link
    else:
      print(f"Failed to upload file: {audio_url.text}")
      return None

  except Exception as e:
    print(f"An error occurred: {e}")
    return None
  
def ai_voice():

  try:
    mytext = response.text
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("technews.mp3")
   

    # os.system("technews.mp3")

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
  temp_link = upload_audio_temp("technews.mp3")
  if temp_link:
      whatsapp_chat(temp_link)
  else:
      print("Failed to upload audio. WhatsApp message not sent.")