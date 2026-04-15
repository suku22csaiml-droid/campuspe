import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file. Copy .env.example to .env and add your key.")
    exit(1)

client = OpenAI(api_key=api_key)

print("OpenAI Chat - Enter your prompt (or 'quit' to exit):")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print(response.choices[0].message.content)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

