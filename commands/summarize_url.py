import sqlite3
from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_article import get_readable

def insert_article(url, article, summary):
    conn = sqlite3.connect('telegram_uat.db')
    c = conn.cursor()
    c.execute("INSERT INTO articles (url, article, summary) VALUES (?, ?, ?)", (url, article, summary))
    conn.commit()
    conn.close()

# send a large message
async def send_paginated_message(chat_id, context, message):
    i = 0
    while i < len(message):
      await context.bot.send_message(chat_id, text=message[i:i+3000])
      i += 3000

# return the first and last words as a string
def get_first_and_last_words(text):
    words = text.split()
    word_count = len(words)
    return f'{word_count} words from "' + ' '.join(words[:3]) + ' ... ' + ' '.join(words[-3:]) +  '" /view_source'

async def summarize_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # acknowledge message request
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Generating Summary")

    # clear user_data state
    context.user_data['state'] = {}
    chat_id = update.effective_chat.id
    context.user_data['state'][chat_id] = {"mode": "article"}

    # send the summary
    URL = update.message.text
    page = get_readable(URL)
    source = get_first_and_last_words(page)
    # context.user_data['state'][chat_id] = {"message": [{'role':'system', 'content': 'You are a bot that summarises the users input. Reduce it down to 2 sentences'}, {"role": "user", "content": page}]}
    context.user_data['state'][chat_id]["message"] = [{"role": "user", "content": f'Summarise the following article in triple backticks into 2 sentences: ```#{page}```'}]
    context.user_data['state'][chat_id]['source'] = page
    summary = summarize_text(context.user_data['state'][chat_id]['message'])
    insert_article(URL, page, summary)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary + "\n\n" + source)
