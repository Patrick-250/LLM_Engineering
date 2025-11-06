from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()    #funny enough that LiteLLM also just picks the loaded env... but what if i have more? thats whre having model_provider parameter helps

response=completion(model="openai/gpt-5-nano",messages=[{"role":"user","content":"write me  a poem about project managers"}],
stream=True,

)
for chunk in response:
    if chunk.choices and chunk.choices[0].delta.get("content"):
        print(chunk.choices[0].delta.content,end="",flush=True)

