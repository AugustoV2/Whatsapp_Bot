from twilio.rest import Client
import os
from dotenv import load_dotenv
from gtts import gTTS
import requests
import google.generativeai as genai
import requests



load_dotenv() 


def whatsapp_chat():
  

  try:
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    print(auth_token)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM"),
    body='Tech News Fileee',
    
    to='whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")
    )

    print("hello")
    print(audio_url)

   
    message = client.messages.create(
    from_='whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM"),
    
   
    media_url=[audio_url],
  
    to='whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")
    )

    print(message.sid)
  
  except Exception as e:
    print(f"An error occurred: {e}")





def upload_audio_to_envs(file_path):
    print("Starting upload...")

    try:
        url = "https://envs.sh"
        
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'audio/mpeg')}
            
            response = requests.post(url, files=files, timeout=30)

        if response.status_code != 200:
            print("Error uploading file")
            return {'error': 'Error uploading file'}

       
        uploaded_url = response.text.strip()
        print(f"Uploaded URL: {uploaded_url}")

       
        if not uploaded_url.startswith("http"):
            print("Invalid upload response")
            return {'error': 'Invalid upload response'}

        return uploaded_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': 'Error uploading file'}



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
  audio_url = upload_audio_to_envs("technews.mp3")
  print(audio_url)
  whatsapp_chat()

  
 