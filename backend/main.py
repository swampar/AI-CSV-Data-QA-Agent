from fastapi import FastAPI

app = FastAPI(
    title="AI CSV Data Q&A Agent",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "AI CSV Data Q&A Agent is Running!"
    }