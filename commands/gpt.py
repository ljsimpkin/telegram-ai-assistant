from .common import Update, ContextTypes
from models.gpt_conversation import gpt_start

async def gpt_command(update: Update, context: ContextTypes.context):
    state = context.user_data['state']
        chat_id = update.effective_chat.id
        if chat_id not in state:
            state[chat_id] = {}

        if "message" not in state[chat_id]:
            state[chat_id]["message"] = []

        # Remove the command from the message text e.g. /gpt
        message_text = ' '.join(update.message.text.split()[1:])

        state[chat_id]["message"].append({"role": "user", "content": message_text})

        response = await gpt_start(state[chat_id])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
