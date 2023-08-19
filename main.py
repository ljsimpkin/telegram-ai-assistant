import logging
import os
from telegram import Update, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a directory for voice messages if it doesn't exist
if not os.path.exists('voice_messages'):
    os.makedirs('voice_messages')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # upload and send an image
    await context.bot.send_document(chat_id=update.effective_chat.id, document='test.png')
    # send a url image
    await context.bot.send_document(chat_id=update.effective_chat.id, document='https://python-telegram-bot.org/static/testfiles/telegram.gif')
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
    file_id = update.message.voice.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('voice_messages/voice_message.ogg')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    from env import TOKEN
    application = ApplicationBuilder().token(TOKEN).build()

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
