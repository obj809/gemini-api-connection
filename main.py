# main.py

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-2.5-flash"

client = genai.Client()

response = client.models.generate_content(
    model=MODEL,
    contents="Explain how AI works in a few words."
)

print(response.text)