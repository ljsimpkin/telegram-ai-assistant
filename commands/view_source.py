from .common import Update, ContextTypes
import json

async def view_source(update: Update, context: ContextTypes.context):
  # check if the state has summarised a url
  # if hasattr(context.user_data, 'message') and hasattr(context.user_data.message[0], 'role') and context.user_data.message[0].role == 'system':
  #     await context.bot.send_message(chat_id=update.effective_chat.id, text="URL found yeha!")
  # else:
  #     await context.bot.send_message(chat_id=update.effective_chat.id, text="No source found. Have you summarized a url?")

  # import pdb; pdb.set_trace()

  chat_id = update.effective_chat.id


  if 'state' in context.user_data:
      await context.bot.send_message(chat_id=update.effective_chat.id, text="URL found yeha!")
  else:
      await context.bot.send_message(chat_id=update.effective_chat.id, text="No source found. Have you summarized a url?")

  i = 0
  while i < len(json.dumps(context.user_data)):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=json.dumps(context.user_data)[i:i+3000])
    i += 3000
