import openai
import os
from .bible_service import search_verses
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_language(text: str):
    """
    Detects the language of the input text using OpenAI.
    """
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": f"Detect the language of this text: {text}. Just return the language name."}],
            temperature=0
        )
        detected_language = response.choices[0].message.content.strip()
        print(f"Detected Language: {detected_language}")
        return detected_language
    except Exception as e:
        print(f"Error detecting language: {e}")
        return "English"  # Default to English if detection fails

def translate_sections(language: str):
    """
    Translates sermon section headers to the detected language.
    """
    try:
        client = openai.OpenAI()
        prompt = f"""
        Translate the following sermon section headers into {language}:
        Sermon Title
        Introduction
        Main Points
        Bible Verses
        Conclusion

        Return only the translated list in order.
        """
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        translations = response.choices[0].message.content.strip().split("\n")
        return translations
    except Exception as e:
        print(f"Error translating headers: {e}")
        return ["Sermon Title", "Introduction", "Main Points", "Bible Verses", "Conclusion"]

def generate_sermon_outline(topic: str):
    """
    Generates a sermon outline in the detected language with translated section headers.
    """
    try:
        language = detect_language(topic)  # Auto-detect language
        section_titles = translate_sections(language)  # Get translated section headers

        prompt = f"""
        Generate a structured sermon outline on '{topic}' in {language}.
        Use the following translated headers in **Markdown** format:
        - **{section_titles[0]}** (bold title)
        - **{section_titles[1]}** (short introduction paragraph)
        - **{section_titles[2]}** (3 main sermon points formatted with `-`)
        - **{section_titles[3]}** (3 Bible verses in blockquotes `>` with the verse reference in bold)
        - **{section_titles[4]}** (final conclusion paragraph)

        Return the output in full **Markdown formatting**.
        """

        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        outline_text = response.choices[0].message.content
        return outline_text, language
    except Exception as e:
        print(f"Error in OpenAI request: {e}")
        return "Error generating sermon outline", "English"

def find_bible_verses(theme: str):
    return search_verses(theme)
