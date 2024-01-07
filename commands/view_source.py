from .common import Update, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

# TO DO: It would be better to have a unique view_source link that takes the user to the article in question like how a website would do when accessing a database value
async def view_source(update: Update, context: ContextTypes.context):
  chat_id = update.effective_chat.id

  if 'mode' in context.user_data['state'][chat_id] and context.user_data['state'][chat_id]['mode'] == "article":  
      source = "Source: " + context.user_data['state'][chat_id]['source']
      i = 0
      while i < len(source):
        if i+3000 >= len(source):  # This is the last chunk of the source
            # Create two buttons
            button_yes = InlineKeyboardButton("Yes", callback_data='button_yes')
            button_no = InlineKeyboardButton("No", callback_data='button_no')
            # Create a keyboard with the buttons
            keyboard = InlineKeyboardMarkup([[button_yes, button_no]])
            # Send the message with the keyboard
            await context.bot.send_message(chat_id=update.effective_chat.id, text=source[i:i+3000], reply_markup=keyboard)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=source[i:i+3000])
        i += 3000
  else:
      await context.bot.send_message(chat_id=update.effective_chat.id, text="No source found. Have you summarized a url?")
