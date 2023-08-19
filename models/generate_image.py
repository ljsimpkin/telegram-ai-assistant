    
import requests
from env import HUGGING_FACE_TOKEN

import os
from telegram import Update
from telegram.ext import ContextTypes

IMAGE_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

def save_image(image_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(image_bytes)

def get_image(payload):
	response = requests.post(IMAGE_API_URL, headers={"Authorization": HUGGING_FACE_TOKEN}, json=payload)
	return response.content

def text_to_image(text):
  return get_image({
    "inputs": text,
  })

async def generate_image(update, context):
    # Generate an image from the text
    text = ' '.join(context.args)
    # import pdb; pdb.set_trace()
    image_bytes = text_to_image(text)
    # respond with the generated image
    return save_image(image_bytes, './downloads/output_image.jpg')
  