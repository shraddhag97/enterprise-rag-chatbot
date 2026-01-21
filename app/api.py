from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION
from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.rag_pipeline import RAGPipeline
from app.chatbot.memory import add_user_message, get_history

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

rag = RAGPipeline()


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Enterprise RAG Chatbot is running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    add_user_message(request.session_id, request.message)

    history = get_history(request.session_id)

    answer = rag.answer(
        question=request.message,
        history=history[:-1]  # exclude current question
    )

    return ChatResponse(
        session_id=request.session_id,
        answer=answer,
        sources=["sample.txt"],
        confidence=0.9
    )