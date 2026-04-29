"""
Day 1: First real Gemini API call.
Asks Gemini to explain what an AI PM does differently from a regular PM.
"""

import os
from google import genai
from dotenv import load_dotenv

# Load the API key from the .env file at the repo root
load_dotenv(dotenv_path="../.env")

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# The prompt — substantive enough to be meaningful, short enough to debug fast
prompt = """In 3 sentences, explain what an AI Product Manager does that a regular Product Manager doesn't.
Be concrete and avoid buzzwords. Mention something about evals."""

# Call the model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

# Print the response
print("=" * 60)
print("PROMPT:")
print(prompt)
print("=" * 60)
print("RESPONSE:")
print(response.text)
print("=" * 60)