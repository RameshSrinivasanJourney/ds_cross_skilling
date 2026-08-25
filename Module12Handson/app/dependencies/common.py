from fastapi import Header, HTTPException, status

from app.core.config import API_KEY
from app.services.llm_service import (
    LLMService,
)


def get_llm_service() -> LLMService:
    """Provide an LLM service instance."""

    return LLMService()


def verify_api_key(
    x_api_key: str | None = Header(
        default=None
    ),
) -> str:

    if x_api_key != API_KEY:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )

    return x_api_key