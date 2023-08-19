import requests
from env import HUGGING_FACE_TOKEN

HUGGING_FACE_TOKEN = "Bearer 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"

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": HUGGING_FACE_TOKEN}

def summarise_text(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = summarise_text({
	"inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building",
})

print(output)