from .common import Update, ContextTypes

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


from .common import Update, ContextTypes
from models.transcribe_audio import transcribe_audio
from models.summarize_gpt import summarize_text
from models.get_html import get_static_website, get_readable

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print ("\n\nurl summariser lesh gooo\n\n")

    # URL = "https://en.wikipedia.org/wiki/New_Zealand"
    URL = update.message.text
    # page = get_static_website(URL)
    page = get_readable(URL)[:4000]

    # import pdb; pdb.set_trace()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=page)

    summary = summarize_text(page)
    summary = "Summary: " + summary
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)