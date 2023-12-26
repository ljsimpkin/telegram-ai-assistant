import logging
import os
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from env import TELEGRAM_TOKEN
from commands.start import start
from commands.image import image
from commands.say import say
from commands.echo import echo
from commands.caps import caps
from commands.voice_handler import voice_handler
from commands.unknown import unknown
from commands.summarize_url import summarize_url
from commands.handle_input_text import handle_input_text
from commands.gpt import gpt_command
from commands.state import get_state

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a directory for downloads if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # state returns the state object
    state_handler = CommandHandler('state', get_state)
    application.add_handler(state_handler)

    gpt_handler = CommandHandler('gpt', gpt_command)
    application.add_handler(gpt_handler)

    # Handles all incoming plain text and triggers respective services
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_input_text)
    application.add_handler(text_handler)
    
    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    image_handler = CommandHandler('img', image)
    application.add_handler(image_handler)
    
    text_to_speech_handler_main = CommandHandler('say', say)
    application.add_handler(text_to_speech_handler_main)

    image_handler = CommandHandler('url', summarize_url)
    application.add_handler(image_handler)

    voice_message_handler = MessageHandler(filters.VOICE, voice_handler)
    application.add_handler(voice_message_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()
