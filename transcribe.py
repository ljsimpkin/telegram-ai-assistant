import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-tiny"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# output = query("./voice_messages/voice_message.ogg")

# print(output)


import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

image_bytes = query({
	"inputs": "Astronaut riding a horse",
})

# You can access the image with PIL.Image for example
import os
def save_image(image_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(image_bytes)

# Save the image to the local directory
save_image(image_bytes, os.path.join(os.getcwd(), 'output_image.jpg'))
