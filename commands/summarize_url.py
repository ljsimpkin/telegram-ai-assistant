from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_article import get_readable

# async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     URL = update.message.text
#     page = get_readable(URL)
#     summary = summarize_text(page)
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)
#     i = 0
#     # message back the source of the summarization
#     while i < len(page):
#       await context.bot.send_message(chat_id=update.effective_chat.id, text=page[i:i+3000])
#       i += 3000

async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # clear user_data state
    context.user_data['state'] = {}
    chat_id = update.effective_chat.id
    URL = update.message.text
    page = get_readable(URL)
    
    CODE_FLAG= f'You are a bot that summarises the users input. Reduce it down to 2 sentences'
    context.user_data['state'][chat_id] = {"message": [{'role':'system', 'content': CODE_FLAG}, {"role": "user", "content": page}]}
    
    summary = summarize_text(context.user_data['state'][chat_id]['message'])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)
    i = 0
    # message back the source of the summarization
    while i < len(page):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=page[i:i+3000])
      i += 3000

    
