import os
from .common import Update, ContextTypes
from models.hugging_face import query, get_image

def save_image(image_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(image_bytes)
        
def text_to_image(text):
  image_bytes = get_image({
    "inputs": text,
  })
  return save_image(image_bytes,  './downloads/output_image.jpg')

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # download the voice message
    file_id = update.message.voice.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('downloads/voice_message.ogg')
    # transcribe the voice message
    output = query("./downloads/voice_message.ogg")
    # respond with the transcription
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=output["text"]
    )
    # Generate an image from the transcription
    text_to_image(output["text"])
    # respond with the generated image
    await context.bot.send_document(chat_id=update.effective_chat.id, document='./images/output_image.jpg')
