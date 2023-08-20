from .common import Update, ContextTypes
from models.transcribe_audio import transcribe_audio
from models.summarize_gpt import summarize_text
from models.getHTML import get_static_website

async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print ("\n\nurl summariser lesh gooo\n\n")

    # URL = "https://en.wikipedia.org/wiki/New_Zealand"
    URL = ' '.join(context.args)
    page = get_static_website(URL)

    # import pdb; pdb.set_trace()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=page)

    summary = summarize_text(page)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)
    # message = await transcribe_audio(update, context)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=message["text"])
    # 
    # summary = "Summary: " + summary
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)