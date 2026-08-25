from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import (
    StreamingResponse,
)

from app.dependencies.common import (
    get_llm_service,
    verify_api_key,
)
from app.models.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.llm_service import (
    LLMService,
)


router = APIRouter(
    prefix="/api/v1/chat",
    tags=["chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    _: str = Depends(
        verify_api_key
    ),
    llm: LLMService = Depends(
        get_llm_service
    ),
):

    answer = await llm.generate_async(
        request.question
    )

    return ChatResponse(
        answer=answer,
        model=llm.model,
    )


@router.post(
    "/stream"
)
async def stream_chat(
    request: ChatRequest,
    _: str = Depends(
        verify_api_key
    ),
    llm: LLMService = Depends(
        get_llm_service
    ),
):

    return StreamingResponse(
        llm.stream(
            request.question
        ),
        media_type="text/plain",
    )