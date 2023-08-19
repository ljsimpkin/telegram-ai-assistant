import os
from .common import Update, ContextTypes
from models.generate_image import generate_image

async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await generate_image(update, context)
  await context.bot.send_document(chat_id=update.effective_chat.id, document='./downloads/output_image.jpg')