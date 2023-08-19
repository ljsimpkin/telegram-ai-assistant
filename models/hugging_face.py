import requests
from env import HUGGING_FACE_TOKEN

import os
from telegram import Update
from telegram.ext import ContextTypes

TRANSCRIPTION_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
IMAGE_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": HUGGING_FACE_TOKEN}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(TRANSCRIPTION_API_URL, headers=headers, data=data)
    return response.json()

def get_image(payload):
	response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
	return response.content

def save_image(image_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(image_bytes)
        
def text_to_image(text):
  image_bytes = get_image({
    "inputs": text,
  })
  return save_image(image_bytes,  './downloads/output_image.jpg')

def test():
  return "\n\n\ntest\n\n\n"

async def summarise_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # download the voice message
    file_id = update.message.voice.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('downloads/voice_message.ogg')
    # transcribe the voice message
    return query("./downloads/voice_message.ogg")