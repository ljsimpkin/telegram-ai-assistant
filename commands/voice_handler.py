import os
from .common import Update, ContextTypes
from models.hugging_face import summarise_audio, test

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await summarise_audio(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message["text"])