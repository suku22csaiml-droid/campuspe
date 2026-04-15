import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv('HF_API_KEY')
# HF token optional for public models, but recommended for rate limits

client = InferenceClient(api_key=api_key)

print("Hugging Face Chat - Enter your prompt (or 'quit' to exit):")
while True:
    prompt = input("> ")
    if prompt.lower() == 'quit':
        break
    try:
        response = client.text_generation(
            prompt,
            model="HuggingFaceH4/zephyr-7b-beta",
            max_new_tokens=200,
            temperature=0.7
        )
        print(response)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

