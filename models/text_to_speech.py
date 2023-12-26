from pathlib import Path
from openai import OpenAI
client = OpenAI()



async def text_to_speech(text):
	print(text)
	
	speech_file_path = Path(__file__).parent / "speech.mp3"
	response = client.audio.speech.create(
  	model="tts-1",
  	voice="onyx",
  	input=text
	)

	return response.stream_to_file(speech_file_path)

#text_to_speech("this is a new string")
