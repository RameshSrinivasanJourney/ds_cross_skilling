from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.ai_service import AIService

router = APIRouter(prefix="/chat", tags=["Chat"])

ai_service = AIService()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    result = ai_service.get_response(
        request.prompt,
        request.model,
        request.temperature
    )

    return ChatResponse(**result)