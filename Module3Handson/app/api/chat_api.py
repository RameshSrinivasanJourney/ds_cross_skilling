from fastapi import APIRouter

from app.models.chat_models import (ChatRequest,ChatResponse)
from app.services.ai_service import (AIService)
from app.services.conversation_service import (ConversationService)

from fastapi.responses import StreamingResponse
from app.services.streaming_service import StreamingService

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

    
@router.post("/chat/stream")
def stream_chat():

    return StreamingResponse(
        content=[],
        media_type="text/event-stream"
    )


@router.post("/chat/streamSSE")
def stream_chat_sse(request: ChatRequest):

    messages = [
        {
            "role": "user",
            "content": request.message
        }
    ]

    service = StreamingService()

    return StreamingResponse(
        service.stream_chat(messages),
        media_type="text/event-stream"
    )

@router.post("/chat/partial")
def stream_partial(request: ChatRequest):

    messages = [
        {
            "role": "user",
            "content": request.message
        }
    ]

    service = StreamingService()

    return StreamingResponse(
        service.stream_partial(messages),
        media_type="text/event-stream"
    )