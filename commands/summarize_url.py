from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_html import get_readable

async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    URL = update.message.text
    page = get_readable(URL)
    summary = summarize_text(page)
    summary = "Summary: " + summary
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)