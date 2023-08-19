import requests
import openai

MODEL="gpt-3.5-turbo"
MAX_TOKENS=256
TEMPERATURE=1

# CODE_FLAG="You are a bot that summarises the users input. Reduce it half the length"

# CODE_FLAG="As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines: 1 Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness. 2 Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects. 3 Rely strictly on the provided text, without including external information. 4 Format the summary in paragraph form for easy understanding. By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner."

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

def sentence_count(string):
    return len(string.split('.')) 

def summarize_text(text):
    count = sentence_count(text)
    length = f'{count // 5} sentences' if count > 3 else "1 sentence"
    # import pdb; pdb.set_trace()
    CODE_FLAG= f'You are a bot that summarises the users input. Reduce it down to {length}'
    input_messages=[{'role':'system', 'content': CODE_FLAG}, {"role": "user", "content": text}]
    response = interact_with_gpt(input_messages)
    # This is a placeholder implementation. We'll replace this with a call to the actual API.
    return response
