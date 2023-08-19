import logging
import os
from telegram import Update, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

import requests
from env import TELEGRAM_TOKEN, HUGGING_FACE_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": HUGGING_FACE_TOKEN}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

IMAGE_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

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
  return save_image(image_bytes,  './images/output_image.jpg')

# Create a directory for voice messages if it doesn't exist
if not os.path.exists('voice_messages'):
    os.makedirs('voice_messages')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # upload and send an image
    await context.bot.send_document(chat_id=update.effective_chat.id, document='./images/output_image.jpg')
    # upload an audio file
    # await context.bot.send_document(chat_id=update.effective_chat.id, document='./voice_messages/voice_message.ogg')
    # send a url image
    # await context.bot.send_document(chat_id=update.effective_chat.id, document='https://python-telegram-bot.org/static/testfiles/telegram.gif')
    # respond with a text
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # download the voice message
    file_id = update.message.voice.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('voice_messages/voice_message.ogg')
    # transcribe the voice message
    output = query("./voice_messages/voice_message.ogg")
    # respond with the transcription
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=output["text"]
    )
    # Generate an image from the transcription
    text_to_image(output["text"])
    # resoind with the generated image
    await context.bot.send_document(chat_id=update.effective_chat.id, document='./images/output_image.jpg')
    

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    voice_message_handler = MessageHandler(filters.VOICE, voice_handler)
    application.add_handler(voice_message_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()
