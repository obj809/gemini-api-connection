# main.py

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-2.5-flash"

client = genai.Client()

response = client.models.generate_content(
    model=MODEL,
    contents="Write a one-sentence bedtime story about a robot who is trying to learn how to dream."
)

print(response.text)