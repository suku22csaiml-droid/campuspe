import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file. Copy .env.example to .env and add your key.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

print("Google Gemini Chat - Enter your prompt (or 'quit' to exit):")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = model.generate_content(prompt)
        print(response.text)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

