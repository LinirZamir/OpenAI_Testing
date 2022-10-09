import os 
from dotenv import load_dotenv
from gpt import GPT, Example, set_openai_key

## Loading .env file with data
load_dotenv()

set_openai_key(os.getenv("OPENAI_API_KEY"))
gpt = GPT()
prompt = "eggs and flowers are the ingredients of a cake"
print(gpt.get_top_reply(prompt))

gpt.add_example(Example("chocolate cake is made from ", "2 + 2 = 4"))
print(gpt.get_top_reply(prompt))