from fastapi import APIRouter

from app.models.chat_models import (ChatRequest,ChatResponse)
from app.services.ai_service import (AIService)
from app.services.conversation_service import (ConversationService)


router = APIRouter()

@router.post(
    "/chat",
    response_model=ChatResponse
)

def chat(request: ChatRequest):

    ConversationService.add_assistant_message(
        request.message
    )

    answer = AIService.ask()

    ConversationService.add_assistant_message(
        answer
    )

    return ChatResponse(
        response=answer
    )

    
