# How to Guide: Gemini API Connection

## Description

A Python quickstart guide for getting started with the Google Gemini API.

## Requirements

- Python 3.10+
- A Google Gemini API key

## main.py

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY not set")

MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=gemini_api_key)

response = client.models.generate_content(
    model=MODEL,
    contents="Write a one-sentence bedtime story about a robot who is trying to learn how to dream."
)

print(response.text)
```

## Build Steps


1) Create a Google AI account
[https://ai.google.dev/](https://ai.google.dev/)


2) Create a Gemini API key
Once logged in:
[https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)


3) Clone this repo
```bash
git clone https://github.com/obj809/gemini-api-connection
```
```bash
cd gemini-api-connection
```


4) Create a virtual environment
```bash
python -m venv venv
```


5) Activate the virtual environment
macOS / Linux
```bash
source venv/bin/activate
```
Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```


6) Install requirements
```bash
pip install -r requirements.txt
```

Minimum dependencies:
```bash
pip install google-genai python-dotenv
```


7) Create a .env file in the project root
```env
GEMINI_API_KEY=your_api_key_here
```

8) Run main.py
```bash
python main.py
```


## Links

- [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)

- [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)