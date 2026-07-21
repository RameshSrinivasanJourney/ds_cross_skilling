from fastapi import APIRouter

from app.models.embedding_models import EmbeddingRequest

from app.services.faiss_service import FAISSService


faiss_router = APIRouter(

    prefix="/faiss",

    tags=["FAISS Search"]

)

service = FAISSService()


@faiss_router.post("/search")
def search(

    request: EmbeddingRequest

):

    return {

        "query": request.text,

        "results": service.search(

            request.text

        )

    }