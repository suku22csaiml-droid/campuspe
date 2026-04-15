import os
from dotenv import load_dotenv
import cohere

load_dotenv()

api_key = os.getenv('COHERE_API_KEY')
if not api_key:
    print("Error: COHERE_API_KEY not found in .env file. Copy .env.example to .env and add your key.")
    exit(1)

co = cohere.Client(api_key=api_key)

print("Cohere Chat - Enter your prompt (or 'quit' to exit):")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = co.chat(
            message=prompt,
            model="command-r-plus",
            temperature=0.3
        )
        print(response.text)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

