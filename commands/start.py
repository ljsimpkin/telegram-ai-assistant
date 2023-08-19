import os
from .common import Update, ContextTypes

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
