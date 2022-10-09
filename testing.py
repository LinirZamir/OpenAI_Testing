import os 
from dotenv import load_dotenv
import openai

## Loading .env file with data
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)
