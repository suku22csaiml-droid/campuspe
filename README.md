# campuspe - Generative AI API Integrations

This repository fulfills the assignment for integrating multiple Generative AI APIs (OpenAI, Groq, Ollama, Hugging Face, Google Gemini, Cohere).

Each Python script provides an interactive chat interface:
- Accepts user input prompts
- Sends requests to the respective API
- Displays AI-generated responses
- Handles errors (missing keys, network issues, etc.)
- Uses environment variables for API keys (no hardcoding)

## Files
- `*_chat.py`: Individual API integration scripts
- `requirements.txt`: Python dependencies
- `.env.example`: Template for API keys
- `README.md`: This file
- `screenshots/`: Add your test screenshots here (create dir)

## Setup

### 1. API Keys
Copy `.env.example` to `.env` and fill in your keys:

```
OPENAI_API_KEY=sk-...  # https://platform.openai.com/api-keys
GROQ_API_KEY=gsk_...   # https://console.groq.com/keys
HF_API_KEY=hf_...      # https://huggingface.co/settings/tokens (optional but recommended)
GOOGLE_API_KEY=AIza... # https://makersuite.google.com/app/apikey (Gemini)
COHERE_API_KEY=...     # https://dashboard.cohere.com/api-keys
```
**Ollama**: Local only. Install from https://ollama.com/download , then `ollama pull llama3` and `ollama serve`.

### 2. Python Environment (Windows)
```
cd ai_api_integrations
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 3. Test Each Script
```
python openai_chat.py
python groq_chat.py
python ollama_chat.py
python hf_chat.py
python gemini_chat.py
python cohere_chat.py
```
- Enter prompts interactively
- Type `quit` to exit
- Take screenshots of outputs for submission

## Models Used (Accessible/Free tiers)
| Script | Model | Notes |
|--------|-------|-------|
| openai | gpt-3.5-turbo | Cheap, reliable |
| groq | llama-3.1-8b-instant | Fast inference |
| ollama | llama3 | Local (pull model first) |
| hf | zephyr-7b-beta | Open model |
| gemini | gemini-1.5-flash | Free tier |
| cohere | command-r-plus | Powerful |

## Error Handling
- Checks for missing API keys upfront
- Catches API/network exceptions
- User-friendly messages

## GitHub Submission
1. `git init`
2. `git add .`
3. `git commit -m "AI API integrations complete"`
4. `git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git`
5. `git push -u origin main`
6. Make repo **public**
7. Submit repo URL on LMS

## Screenshots
Create `screenshots/` folder and add images:
- ![OpenAI](screenshots/openai_output.png)
- etc.

All requirements met: separate files, user input/response, error handling, env vars, requirements.txt, README.

=======
# campuspe
>>>>>>> 2bbea64785858b027415c3c099e378af4e233aa0
