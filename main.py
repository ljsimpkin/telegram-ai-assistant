import logging
import os
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from env import TELEGRAM_UAT_TOKEN
from commands.start import start
from commands.image import image
from commands.text_to_speech_handler import text_to_speech_handler
from commands.echo import echo
from commands.caps import caps
from commands.voice_handler import voice_handler
from commands.unknown import unknown
from commands.summarize_url import summarize_url

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a directory for downloads if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_UAT_TOKEN).build()

    from commands.history import history

    state = {}

    # def store_message(update: Update, context: ContextTypes.Context):
    #     chat_id = update.effective_chat.id
    #     if chat_id not in state:
    #         state[chat_id] = []
    #     state[chat_id].append(update.message.text)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), summarize_url)
    application.add_handler(echo_handler)
    
    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)

    history_handler = CommandHandler('history', history)
    application.add_handler(history_handler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    image_handler = CommandHandler('img', image)
    application.add_handler(image_handler)
    
    text_to_speech_handler_main = CommandHandler('say', text_to_speech_handler)
    application.add_handler(text_to_speech_handler_main)

    image_handler = CommandHandler('url', summarize_url)
    application.add_handler(image_handler)

    voice_message_handler = MessageHandler(filters.VOICE, voice_handler)
    application.add_handler(voice_message_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()
