


# 📄 AI-Generated Tech News to WhatsApp (with Audio)

## Overview
This project uses **Gemini AI** to generate a short tech news summary, converts the text into **speech (audio)** using **gTTS**, uploads the audio to a hosting service, and finally **sends it via WhatsApp** using **Twilio's API**.

---

## 📚 Module Dependencies
- `twilio` (for WhatsApp messaging)
- `gtts` (for text-to-speech conversion)
- `requests` (for uploading files and HTTP requests)
- `google-generativeai` (to interact with Gemini AI)
- `dotenv` (to securely manage environment variables)

---

## 🔑 Environment Variables Required (`.env`)
| Variable Name          | Purpose                                      |
|:------------------------|:---------------------------------------------|
| `account_sid`           | Twilio Account SID                          |
| `auth_token`            | Twilio Auth Token                           |
| `TWILIO_WHATSAPP_FROM`  | Sender's WhatsApp number via Twilio         |
| `TWILIO_WHATSAPP_TO`    | Receiver's WhatsApp number                  |
| `GEMINI_API_KEY`        | API key to access Google Gemini API         |

---

## 🛠️ Functions Description

### 1. `gemini()`
> **Purpose**: Generates a 100-word tech news summary using Google Gemini AI.  
> **Returns**: `response.text` (summary content)

### 2. `ai_voice()`
> **Purpose**: Converts the Gemini-generated text into an audio file (`technews.mp3`) using **gTTS**.  
> **Output**: Saves a local MP3 file.

### 3. `upload_audio_to_envs(file_path)`
> **Purpose**: Uploads the generated MP3 file to a hosting service.  
> **Input**: Path to the MP3 file.  
> **Returns**: Public URL of the uploaded audio.

### 4. `whatsapp_chat()`
> **Purpose**: Sends two WhatsApp messages via Twilio:
> - Text message ("Fileeeee")
> - Audio message with the uploaded MP3 link

---

## 🧩 Workflow (Main Execution)

1. Generate tech news summary via `gemini()`
2. Convert summary to speech using `ai_voice()`
3. Upload the audio file with `upload_audio_to_envs()`
4. Send the audio link via `whatsapp_chat()`



---

## 📌 Important Notes
- Ensure your Twilio account has WhatsApp access enabled and verified.
- Uploaded audio files must be publicly accessible for WhatsApp to fetch.

---

## 📬 Contact
For any queries or suggestions, feel free to reach out! 🚀




