from openai import OpenAI
import os
from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

client = OpenAI()

MODEL="gpt-4-1106-preview"
MAX_TOKENS=500
TEMPERATURE=1

def setup_openai():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environmental variable.")
    client.api_key = api_key

def interact_with_gpt(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return response.choices[0].message.content

# this function takes message and state, appends things to the state and returns the chatgpt
def interact_with_gpt(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return response.choices[0].message.content

async def gpt_start(state):
    setup_openai()
    conversation = state["message"]
    # history = InMemoryHistory()
    
    response = interact_with_gpt(messages=conversation)
    conversation.append({"role": "assistant", "content": response})
    # print(Fore.GREEN + "ChatGPT: " + response)
    state["message"] = conversation
    
    return response