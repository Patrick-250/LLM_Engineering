from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()    #funny enough that LiteLLM also just picks the loaded env... but what if i have more? thats whre having model_provider parameter helps

response=completion(model="openai/gpt-5-nano",messages=[{"role":"user","content":"tell me a joke about project managers"}])
print(response.choices[0].message.content)