import sqlite3
from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_article import get_readable

def check_url_exists(url):
    conn = sqlite3.connect('telegram_uat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM articles WHERE url=?", (url,))
    result = c.fetchone()
    conn.close()
    return result

def insert_article(chat_id, url, article, summary):
    conn = sqlite3.connect('telegram_uat.db')
    c = conn.cursor()
    c.execute("INSERT INTO articles (chat_id, url, article, summary) VALUES (?, ?, ?, ?)", (chat_id, url, article, summary))
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

    URL = update.message.text

    # clear user_data state
    context.user_data['state'] = {}
    chat_id = update.effective_chat.id
    context.user_data['state'][chat_id] = {"mode": "article", "url" : URL}

    existing_article = check_url_exists(URL)
    if existing_article:
        page = existing_article[3]
        summary = existing_article[4]
        source = get_first_and_last_words(page)
        context.user_data['state'][chat_id]["message"] = [{"role": "user", "content": f'Summarise the following article in triple backticks into 2 sentences: ```#{page}```'}]
        context.user_data['state'][chat_id]['source'] = page
    else:
        page = get_readable(URL)
        source = get_first_and_last_words(page)
        context.user_data['state'][chat_id]["message"] = [{"role": "user", "content": f'Summarise the following article in triple backticks into 2 sentences: ```#{page}```'}]
        context.user_data['state'][chat_id]['source'] = page
        summary = summarize_text(context.user_data['state'][chat_id]['message'])
        insert_article(chat_id, URL, page, summary)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary + "\n\n" + source)
