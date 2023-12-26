from .common import Update, ContextTypes
import json

async def get_state(update: Update, context: ContextTypes.context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=(json.dumps(context.user_data)))
