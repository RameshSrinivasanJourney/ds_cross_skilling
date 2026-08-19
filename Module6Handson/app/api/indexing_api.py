from fastapi import APIRouter

from app.models.indexing_models import (
    IndexRequest,
    IndexResponse,
    IndexCountResponse
)

from app.services.indexing_service import (
    IndexingService
)


router = APIRouter(
    prefix="/rag",
    tags=["RAG Indexing"]
)


# ==========================================================
# Index Document
# ==========================================================

@router.post(
    "/index",
    response_model=IndexResponse
)
def index_document(
    request: IndexRequest
):

    response = (
        IndexingService.index_document(
            file_path=request.file_path,

            chunk_size=request.chunk_size,

            chunk_overlap=
                request.chunk_overlap
        )
    )

    return IndexResponse(
        **response
    )


# ==========================================================
# Count
# ==========================================================

@router.get(
    "/index/count",
    response_model=IndexCountResponse
)
def count():

    return IndexCountResponse(

        status="Success",

        total_chunks=
            IndexingService.count()
    )