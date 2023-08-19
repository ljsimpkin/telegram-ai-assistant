from .common import Update, ContextTypes
from models.transcribe_audio import transcribe_audio
from models.summarize_gpt import summarize_text

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await transcribe_audio(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message["text"])
    summary = summarize_text(message["text"])
    summary = "Summary: " + summary
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)