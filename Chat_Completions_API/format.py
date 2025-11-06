import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    print("no api key found in env or did not load successfully")
else:
    print("api key found and loaded successfully")



openai=OpenAI() #by default this looks for openai api key... see line 22-30 in notes.txt to see how to use other frontier models...

message=input("enter your message or something you need help with......     ")
messages=[{"role":"user","content":message}]

response=openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages,
)

print(response.choices[0].message.content)