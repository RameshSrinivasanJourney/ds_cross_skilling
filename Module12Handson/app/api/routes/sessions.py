from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.dependencies.common import (
    verify_api_key,
)
from app.models.session import (
    ChatSessionRequest,
    CreateSessionRequest,
    SessionResponse,
)
from app.services.llm_service import (
    LLMService,
)
from app.sessions.session_store import (
    SESSION_TTL_SECONDS,
    SessionStore,
)


router = APIRouter(
    prefix="/api/v1/sessions",
    tags=["sessions"],
)


def get_session_store() -> SessionStore:
    return SessionStore()


@router.post(
    "",
    response_model=SessionResponse,
)
async def create_session(
    request: CreateSessionRequest,
    _: str = Depends(
        verify_api_key
    ),
    store: SessionStore = Depends(
        get_session_store
    ),
):

    session = store.create_session(
        request.tenant_id
    )

    return SessionResponse(
        tenant_id=session["tenant_id"],
        conversation_id=session[
            "conversation_id"
        ],
        expires_in_seconds=(
            SESSION_TTL_SECONDS
        ),
    )


@router.post(
    "/chat"
)
async def session_chat(
    request: ChatSessionRequest,
    _: str = Depends(
        verify_api_key
    ),
    store: SessionStore = Depends(
        get_session_store
    ),
    llm: LLMService = Depends(
        lambda: LLMService()
    ),
):

    session = store.get_session(
        request.tenant_id,
        request.conversation_id,
    )

    if session is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found or expired.",
        )

    session["messages"].append(
        {
            "role": "user",
            "content": request.message,
        }
    )

    answer = await llm.generate_async(
        request.message
    )

    session["messages"].append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    store.update_session(
        request.tenant_id,
        request.conversation_id,
        session,
    )

    return {
        "tenant_id": request.tenant_id,
        "conversation_id": (
            request.conversation_id
        ),
        "answer": answer,
        "message_count": len(
            session["messages"]
        ),
        "expires_in_seconds": store.ttl(
            request.tenant_id,
            request.conversation_id,
        ),
    }