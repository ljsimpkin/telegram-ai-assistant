import requests
import openai

MODEL="gpt-3.5-turbo"
MAX_TOKENS=256
TEMPERATURE=1

CODE_FLAG="You are a bot that summarises the users input. Reduce it half the length"
# CODE_FLAG="Increase the length of the user input"

def setup_openai():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environmental variable.")
    openai.api_key = api_key

def interact_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return response['choices'][0]['message']['content'].strip()

def summarize_text(text):
    input_messages=[{'role':'system', 'content': CODE_FLAG}, {"role": "user", "content": text}]
    response = interact_with_gpt(input_messages)
    # This is a placeholder implementation. We'll replace this with a call to the actual API.
    return response
