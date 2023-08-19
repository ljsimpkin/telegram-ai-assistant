import os
from .common import Update, ContextTypes
from models.summarise_audio import summarise_audio

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await summarise_audio(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message["text"])