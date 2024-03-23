# NOTE FROM EMILY THIS DOES NTO WORK
# using perplexity ai
# might have to run this line of code: pip install git+https://github.com/nathanrchn/perplexityai.git
# api: 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

from openai import OpenAI
import re

YOUR_API_KEY = "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"

messages = [
    {
        "role": "system",
        "content": (
            # "You are an artificial intelligence assistant and you need to "
            # "engage in a helpful, detailed, polite conversation with a user."
            "You are an artificial intelligence assistant and you are trying to offer suggestions"
            "for a normal person to make little choices in every day life to lower their "
            "greenhouse gas emissions. help them in one sentence, or no more than 20 words"
        ),
    },
    {
        "role": "user",
        "content": (
            "How can I lower my carbon emissions as it relates to food and food consumption?"
        ),
    },
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
response_stream = client.chat.completions.create(
    model="mistral-7b-instruct",
    messages=messages,
    # stream=True
)

for each in response_stream:
    print(response_stream)
    print(type(response_stream))
# print(response_stream)

# for chunk in response_stream:
#     print(f"Chunk: {chunk}")
#     print(f"Type: {type(chunk)}")
#     # print(f"Keys: {list(chunk.keys())}")
#     # print(f"Values: {list(chunk.values())}")
#     print("-" * 20)
text = ""
# for each in response_stream:
#     # chunk = each[0][0][0]
#     chunk_text = each.choices[0].delta.content
#
#     # chunk = each["choices"][0]["delta"].get("content", "")
#     print(response_stream[each])
#     text += chunk

full_response = ""

