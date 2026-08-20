from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="AI Text Summarizer",
    description="AI application for text summarization",
    version="1.0.0"
)

# Load the AI summarization model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "AI Text Summarizer API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.post("/summarize")
def summarize(request: TextRequest):

    result = summarizer(
        request.text,
        max_length=100,
        min_length=20,
        do_sample=False
    )

    return {
        "summary": result[0]["summary_text"]
    }