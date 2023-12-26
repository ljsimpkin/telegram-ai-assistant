from .common import Update, ContextTypes
from models.summarize_gpt import summarize_text
from models.get_youtube_transcript import get_youtube_transcript

async def summarize_youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    URL = update.message.text
    text = get_youtube_transcript(URL)
    # text = "this is a summary test for testing purposes"

    # message back the source of the summarization
    i = 0
    while i < len(text):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=text[i:i+3000])
      i += 3000

    input_messages=[{'role':'system', 'content': 'You are a bot that summarises the users input. Reduce it down to 2 sentences'}, {"role": "user", "content": text}]
    summary = summarize_text(input_messages)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)

    # save summarization as new state
    context.user_data['state'] = {}
    chat_id = update.effective_chat.id
    context.user_data['state'][chat_id] = {"message" : input_messages.append({"role": "assistant", "content": summary})}

    context.user_data['state'][chat_id] = {"message": input_messages}
    