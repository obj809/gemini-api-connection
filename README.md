# How to Guide: Gemini API Connection

## Description

A Python quickstart guide for getting started with the **Google Gemini API** using the official `google-genai` SDK.

---

## Requirements

- Python 3.10+
- A Google Gemini API key

---

## main.py

```python
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-1.5-pro"

# The client reads GEMINI_API_KEY from the environment
client = genai.Client()

response = client.models.generate_content(
    model=MODEL,
    contents="Explain how AI works in a few words."
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


6. Create a .env file in the project root

GEMINI_API_KEY=your_api_key_here


7) Run main.py
```bash
python main.py
```


# Links

- **[Gemini API Models](https://ai.google.dev/gemini-api/docs/models)**  
  Overview of all Gemini models and their capabilities.

- **[Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)**  
  Official guide for getting started with the Gemini API.

- **[google-genai SDK (Python)](https://pypi.org/project/google-genai/)**  
  Python SDK used to interact with the Gemini API.