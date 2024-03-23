import g4f
from g4f.client import Client

# might have to download this as documented here:
# https://github.com/xtekky/gpt4free/blob/main/docs/git.md

# Your code here
# from g4f.client import Client
# #
# client = Client()
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}]
# #    # fill in the rest
# )
# print(response.choices[0].message.content)
from g4f.client import Client
import g4f.providers

client = Client()
response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[{"role": "user", "content": "Hello"}]
)
# print(response.choices[0].message.content)
