from fastapi import APIRouter

from app.models.rag_models import (
    RAGRetrieveRequest,
    RAGRetrieveResponse,
    RAGRetrieveResult,
    RAGCountResponse
)

from app.services.rag_service import RAGService


router = APIRouter(
    prefix="/rag",
    tags=["RAG Retrieve"]
)


# ==========================================================
# Retrieve
# ==========================================================

@router.post(
    "/retrieve",
    response_model=RAGRetrieveResponse
)
def retrieve(
    request: RAGRetrieveRequest
):

    response = RAGService.retrieve(
        query=request.query,

        top_k=request.top_k,

        rerank=request.rerank,

        retrieval_k=request.retrieval_k
    )

    return RAGRetrieveResponse(
        query=response["query"],

        total_results=
            response["total_results"],

        results=[
            RAGRetrieveResult(
                **item
            )
            for item in response["results"]
        ],

        context=response["context"]
    )


# ==========================================================
# Count
# ==========================================================

@router.get(
    "/count",
    response_model=RAGCountResponse
)
def count():

    return RAGCountResponse(
        status="Success",

        total_vectors=
            RAGService.count()
    )