import requests
from env import HUGGING_FACE_TOKEN

TRANSCRIPTION_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
IMAGE_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": HUGGING_FACE_TOKEN}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(TRANSCRIPTION_API_URL, headers=headers, data=data)
    return response.json()

def get_image(payload):
	response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
	return response.content
