from .common import Update, ContextTypes

async def view_source(update: Update, context: ContextTypes.context):
  chat_id = update.effective_chat.id

  if 'state' in context.user_data and chat_id in context.user_data['state'] and 'message' in context.user_data['state'][chat_id] and 'role' in context.user_data['state'][chat_id]['message'][0] and context.user_data['state'][chat_id]['message'][0]['role'] == 'system':
      await context.bot.send_message(chat_id=update.effective_chat.id, text="URL found yeha!")
    
      source = "Source: " + context.user_data['state'][chat_id]['message'][1]['content']

      i = 0
      while i < len(source):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=source[i:i+3000])
        i += 3000
  else:
      await context.bot.send_message(chat_id=update.effective_chat.id, text="No source found. Have you summarized a url?")