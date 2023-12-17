from openai import OpenAI

client = OpenAI()

# MODEL="gpt-3.5-turbo"
MODEL="gpt-4"
MAX_TOKENS=256
TEMPERATURE=1

# CODE_FLAG="You are a bot that summarises the users input. Reduce it half the length"
# CODE_FLAG="As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines: 1 Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness. 2 Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects. 3 Rely strictly on the provided text, without including external information. 4 Format the summary in paragraph form for easy understanding. By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner."

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

def sentence_count(string):
    return len(string.split('.')) 

def summarize_text(input):
    # count = sentence_count(text)
    # length = f'2 sentences' if count > 1 else "1 sentence"
    # import pdb; pdb.set_trace()
    # CODE_FLAG= f'You are a bot that summarises the users input. Reduce it down to {length}'
    # input_messages=[{'role':'system', 'content': CODE_FLAG}, {"role": "user", "content": text}]
    response = interact_with_gpt(input)
    return response
