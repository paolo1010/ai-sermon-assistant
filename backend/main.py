from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from services.openai_service import generate_sermon_outline, find_bible_verses
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

class ThemeRequest(BaseModel):
    theme: str

@app.post("/generate-outline")
def generate_outline(request: TopicRequest):
    outline, detected_language = generate_sermon_outline(request.topic)
    return {"outline": outline, "language": detected_language}

@app.post("/find-verses")
def get_verses(request: ThemeRequest):
    verses = find_bible_verses(request.theme)
    return {"verses": verses}
