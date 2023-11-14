import os
from .common import Update, ContextTypes
from models.text_to_speech import text_to_speech_fun

async def text_to_speech_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  # await generate_image(update, context)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )
    # await context.bot.send_document(chat_id=update.effective_chat.id, document='../models/speech.mp3')
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('./models/speech.mp3', 'rb'))
    text_to_speech_fun("\n\n\n\ntesting!!!\n\n\n\n")
