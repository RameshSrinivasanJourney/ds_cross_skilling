from fastapi import APIRouter

from app.models.embedding_models import EmbeddingRequest
from app.services.semantic_search_service import SemanticSearchService

search_router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


@search_router.post("/semantic")
def semantic_search(
    request: EmbeddingRequest
):

    service = SemanticSearchService()

    results = service.search(
        request.text
    )

    return {

        "query": request.text,

        "results": [

            {
                "similarity": round(score, 4),
                "document": document
            }

            for score, document in results

        ]

    }