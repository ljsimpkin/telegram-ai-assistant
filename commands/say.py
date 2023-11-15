import os
from .common import Update, ContextTypes
from models.text_to_speech import text_to_speech

# this command generates an audio message based on user input
async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Generating audio"
    )
    await text_to_speech(text)
    # await context.bot.send_document(chat_id=update.effective_chat.id, document='../models/speech.mp3')
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('./models/speech.mp3', 'rb'))
    
