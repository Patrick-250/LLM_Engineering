import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    print("No API key found in env or did not load successfully")
else:
    print("API key found and loaded successfully")

openai = OpenAI()

system_prompt = """
You are a specialized personal assistant that generates great speeches for engineering leaders about different AI topics.
You receive the speech location, topic, and audience, then craft a perfect speech based on those 3 parameters.
"""


location = input("Enter the location of your speech: ")
topic = input("Enter your topic: ")
audience = input("Enter your audience: ")


user_message = f"The speech will be delivered at {location}, about {topic}, to an audience of {audience}."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_message}
]

response = openai.chat.completions.create(
    model="gpt-5-nano",  
    messages=messages
)

print(response.choices[0].message.content)
