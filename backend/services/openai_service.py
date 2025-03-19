import openai
import os
from .bible_service import search_verses
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sermon_outline(topic: str):
    try:
        print(f"Generating sermon outline for topic: {topic}")  # Debugging log
        prompt = f"Generate a structured 3-point sermon outline for the topic '{topic}'. Include introduction, 3 main points each with explanation, conclusion, and suggest 3 relevant Bible verses."

        client = openai.OpenAI()  # New OpenAI v1.0+ client format
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        outline_text = response.choices[0].message.content
        return outline_text, []
    except Exception as e:
        print(f"Error in OpenAI request: {e}")  # Print error for debugging
        return "Error generating sermon outline", []

def find_bible_verses(theme: str):
    return search_verses(theme)
