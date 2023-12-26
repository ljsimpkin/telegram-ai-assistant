from .common import Update, ContextTypes
from commands.summarize_url import summarize_url
from commands.summarize_youtube import summarize_youtube
from commands.gpt import gpt_command
import urllib.parse

def is_url(string):
    try:
        result = urllib.parse.urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_youtube_url(string):
    if is_url(string):
        result = urllib.parse.urlparse(string)
        return "youtube.com" in result.netloc or "youtu.be" in result.netloc
    return False

async def handle_input_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_youtube_url(update.message.text):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Summarizing Youtube")
        await summarize_youtube(update,context)
    elif (is_url(update.message.text)):
        await summarize_url(update,context)
    else:
        await gpt_command(update,context)
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
        # await context.bot.send_message(chat_id=update.effective_chat.id, text="No URL Recieved")
