from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_youtube_transcript import get_youtube_transcript

async def summarize_youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    URL = update.message.text
    page = get_youtube_transcript(URL)
    summary = summarize_text(page)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)
    i = 0
    # message back the source of the summarization
    while i < len(page):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=page[i:i+3000])
      i += 3000
        

    