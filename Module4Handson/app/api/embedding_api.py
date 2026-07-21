from fastapi import APIRouter
from app.core.ai_settings import AISettings

from app.models.embedding_models import (
    EmbeddingRequest,
    EmbeddingResponse
)

from app.services.embedding_service import (
    EmbeddingService
)


embedding_router = APIRouter(
    prefix="/embedding",
    tags=["Embeddings"]
)


@embedding_router.post(
    "/generate",
    response_model=EmbeddingResponse
)
def generate_embedding(
    request: EmbeddingRequest
):

    embedding = (
        EmbeddingService.generate_embedding(
            request.text
        )
    )

    return EmbeddingResponse(

        dimensions=len(embedding),

        embedding=embedding[:10],

        model=AISettings.EMBEDDING_MODEL

    )