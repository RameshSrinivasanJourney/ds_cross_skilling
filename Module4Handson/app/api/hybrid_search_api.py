from fastapi import APIRouter

from app.models.embedding_models import EmbeddingRequest
from app.services.hybrid_search_service import HybridSearchService

hybrid_router = APIRouter(
    prefix="/hybrid",
    tags=["Hybrid Search"]
)

service = HybridSearchService()


@hybrid_router.post("/search")
def hybrid_search(request: EmbeddingRequest):

    results = service.search(request.text)

    return {
        "query": request.text,
        "results": results
    }