from fastapi import APIRouter

from app.models.chat_models import (ChatRequest,ChatResponse)
from app.services.ai_service import (AIService)

from fastapi.responses import StreamingResponse
from app.services.streaming_service import StreamingService

from app.prompts.prompt_builder import PromptBuilder

from app.services.scope_service import ScopeService

from app.services.security_service import SecurityService


chat_router = APIRouter(
    tags=["Chat"]
)

@chat_router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    valid, error = SecurityService.validate(
        request.message
    )

    if not valid:

        return ChatResponse(
            response=error
        )

    if not ScopeService.is_hr_related(
        request.message
    ):

        return ChatResponse(
            response=(
                "I'm an HR Assistant and can only "
                "assist with HR-related questions."
            )
        )

    messages = PromptBuilder.build(
        request.message
    )

    answer = AIService.ask(
        messages
    )

    return ChatResponse(
        response=answer
    )
    
@chat_router.post("/chat/stream")
def stream_chat():

    return StreamingResponse(
        content=[],
        media_type="text/event-stream"
    )


@chat_router.post("/chat/streamSSE")
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

@chat_router.post("/chat/partial")
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