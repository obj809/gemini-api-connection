# main.py

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY not set")

MODEL = "gemini-2.5-flash"
PROMPT = "Write a one-sentence bedtime story about a robot who is trying to learn how to dream."

client = genai.Client()

response = client.models.generate_content(
    model=MODEL,
    contents=PROMPT
)

print(response.text)