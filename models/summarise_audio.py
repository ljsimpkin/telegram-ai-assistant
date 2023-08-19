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

async def summarise_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # download the voice message
    file_id = update.message.voice.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('downloads/voice_message.ogg')
    # transcribe the voice message
    return query("./downloads/voice_message.ogg")