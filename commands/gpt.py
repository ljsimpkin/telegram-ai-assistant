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

        # if question is about an article
        if 'mode' in context.user_data['state'][chat_id] and context.user_data['state'][chat_id]['mode'] == "article":
          # does the article answer the question, yes or no?
          # if yes, respond with the answer in quotes
          # if no, respond with error message and make up an answer

          context.user_data['state'][chat_id]["message"].append({"role": "user", "content": f'#{message_text} support your answer with quotes if possible'})
          response = await gpt_start(context.user_data['state'][chat_id])
          await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

          context.user_data['state'][chat_id]["message"].append({"role": "user", "content": f'#{message_text}. Is the question answered by the article? Respond with either "yes" or "no"'})
          response = await gpt_start(context.user_data['state'][chat_id])
          await context.bot.send_message(chat_id=update.effective_chat.id, text=f'#{response}, the article explains that')

          if response == "no" or response == "No":
            print("\n\n\n response is no \n\n\n")
            print(f'response is #{response}')
            context.user_data['state'][chat_id]["message"].append({"role": "user", "content": f'Have a go at answering the question yourself'})
            response = await gpt_start(context.user_data['state'][chat_id])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'I cant find the answer in the article however, #{response}')
            
        else:
          context.user_data['state'][chat_id]["message"].append({"role": "user", "content": message_text})
          response = await gpt_start(context.user_data['state'][chat_id])
          await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
