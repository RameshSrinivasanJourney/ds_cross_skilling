from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=2000)
    model: str = "demo-model"
    temperature: float = 0.7


class ChatResponse(BaseModel):
    success: bool
    model: str
    temperature: float
    response: str
    timestamp: str