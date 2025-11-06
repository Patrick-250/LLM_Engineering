import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()    #funny enough that langchain just picks the loaded env... but what if i have more? thats whre having model_provider parameter helps




llm=init_chat_model(model="gpt-5-nano",model_provider="OPENAI")

response=llm.invoke("tell me a joke about project managers")
print(response)