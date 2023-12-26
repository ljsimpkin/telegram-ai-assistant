from .common import Update, ContextTypes
import json

async def get_state(update: Update, context: ContextTypes.context):
    i = 0
    while i < len(json.dumps(context.user_data)):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=json.dumps(context.user_data)[i:i+3000])
      i += 3000