import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("Error: GROQ_API_KEY not found in .env file. Copy .env.example to .env and add your key.")
    exit(1)

client = Groq(api_key=api_key)

print("Groq Chat - Enter your prompt (or 'quit' to exit):")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        print(response.choices[0].message.content)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

