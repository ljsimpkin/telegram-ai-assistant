from .common import Update, ContextTypes
from models.gpt_conversation import gpt_start

async def gpt_command(update: Update, context: ContextTypes.context):
        message_text = update.message.text
        
        chat_id = update.effective_chat.id
        if 'state' not in context.user_data:
            context.user_data['state'] = {}

        if chat_id not in context.user_data['state']:
            context.user_data['state'][chat_id] = {"message": []}

        # Remove the command from the message text e.g. /gpt
        if update.message.text[0] == '/':
          message_text = ' '.join(update.message.text.split()[1:])


        if 'mode' in context.user_data['state'][chat_id] and context.user_data['state'][chat_id]['mode'] == "article":  
          context.user_data['state'][chat_id]["message"].append({"role": "user", "content": f'#{message_text} support your answer with quotes if a users question is answered by the article'})
        else:
          context.user_data['state'][chat_id]["message"].append({"role": "user", "content": message_text})
 

        response = await gpt_start(context.user_data['state'][chat_id])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
