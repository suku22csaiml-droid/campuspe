import os
from dotenv import load_dotenv
import ollama

# Ollama is local - install from https://ollama.com and run 'ollama pull llama3' first
# No API key needed

print("Ollama Chat (local) - Enter your prompt (or 'quit' to exit). Ensure Ollama running and model pulled.")
print("Tip: ollama pull llama3")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )
        print(response['message']['content'])
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}. Check if Ollama is installed/running and model pulled.")

