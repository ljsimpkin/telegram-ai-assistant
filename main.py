import logging
import os
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from env import TELEGRAM_TOKEN
from commands.start import start
from commands.echo import echo
from commands.caps import caps
from commands.voice_handler import voice_handler
from commands.unknown import unknown

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a directory for voice messages if it doesn't exist
if not os.path.exists('voice_messages'):
    os.makedirs('voice_messages')

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
