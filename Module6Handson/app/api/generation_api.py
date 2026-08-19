from fastapi import APIRouter

from app.models.generation_models import (
    RAGGenerateRequest,
    RAGGenerateResponse,
    RAGSource
)

from app.services.generation_service import (
    GenerationService
)


router = APIRouter(
    prefix="/rag",
    tags=["RAG Generation"]
)


# ==========================================================
# Generate Answer
# ==========================================================

@router.post(
    "/generate",
    response_model=RAGGenerateResponse
)
def generate(
    request: RAGGenerateRequest
):

    response = (
        GenerationService.generate(
            query=request.query,
            top_k=request.top_k
        )
    )

    return RAGGenerateResponse(

        query=response["query"],

        answer=response["answer"],

        context_used=
            response["context_used"],

        sources=[
            RAGSource(
                **source
            )
            for source
            in response["sources"]
        ]
    )