from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from src.RAG.rag_pipeline import answer_question


app = FastAPI(title="GovDocs RAG API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str


class Source(BaseModel):
    source:str 
    document_title: str
    page: str
    version: str
    status: str
    content: str


class AnswerResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]


# Mount the static directory
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/")
def home():
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "GovDocs RAG API is running"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        answer, sources = answer_question(request.question)

        return {
            "question": request.question,
            "answer": answer,
            "sources": sources
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while processing the question."
        )