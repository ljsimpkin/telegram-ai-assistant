def history(update, context):
    chat_id = update.effective_chat.id
    if chat_id in context.bot_data and len(context.bot_data[chat_id]) > 0:
        update.message.reply_text('\n'.join(context.bot_data[chat_id]))
    else:
        update.message.reply_text('No history available.')
