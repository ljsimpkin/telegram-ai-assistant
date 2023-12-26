from .common import Update, ContextTypes

async def clear_state(update: Update, context: ContextTypes.context):
  context.user_data['state'] = {}
  await context.bot.send_message(chat_id=update.effective_chat.id, text="State Cleared")