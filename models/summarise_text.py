import requests
from env import HUGGING_FACE_TOKEN

HUGGING_FACE_TOKEN = "Bearer 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"

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": HUGGING_FACE_TOKEN}

async def summarise_text(text):
	payload = {"inputs": text}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

