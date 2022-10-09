import os 
from dotenv import load_dotenv
from gpt import GPT, Example, set_openai_key

## Loading .env file with data
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
set_openai_key(api_key)
gpt = GPT()
prompt = "integral from a to b of f of x"
print(gpt.get_top_reply(prompt))

gpt.add_example(Example("Two plus two equals four", "2 + 2 = 4"))
print(gpt.get_top_reply(prompt))

gpt.add_example(Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
print(gpt.get_top_reply(prompt))