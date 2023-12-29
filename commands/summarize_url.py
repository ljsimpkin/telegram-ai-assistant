from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_article import get_readable

# message back the source of the summarization
async def send_paginated_message(chat_id, context, message):
    i = 0
    while i < len(message):
      await context.bot.send_message(chat_id, text=message[i:i+3000])
      i += 3000
   

async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # acknowledge message request
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Generating Summary")

    # clear user_data state
    context.user_data['state'] = {}
    chat_id = update.effective_chat.id

    # send the summary
    URL = update.message.text
    page = get_readable(URL)
    context.user_data['state'][chat_id] = {"message": [{'role':'system', 'content': 'You are a bot that summarises the users input. Reduce it down to 2 sentences'}, {"role": "user", "content": page}]}
    summary = summarize_text(context.user_data['state'][chat_id]['message'])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)

    # message back the source of the summarization
    await send_paginated_message(update.effective_chat.id, context, page)
    
