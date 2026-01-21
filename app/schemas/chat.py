from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    session_id: str
    answer: str
    sources: Optional[List[str]] = []
    confidence: Optional[float] = 0.0
