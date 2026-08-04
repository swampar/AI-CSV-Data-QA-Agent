from query_engine import answer_question
from fastapi import FastAPI, UploadFile, File
import shutil
import os
from data_loader import load_csv

app = FastAPI(title="AI CSV Data Q&A Agent")

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI CSV Data Q&A Agent is Running!"}


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = load_csv(file_path)

    return {
        "filename": file.filename,
        "rows": len(df),
        "columns": list(df.columns)
    }
from pydantic import BaseModel

class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(item: Question):
    return answer_question(item.question)