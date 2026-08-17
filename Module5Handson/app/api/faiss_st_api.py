from fastapi import APIRouter

from app.models.faiss_st_models import (
    FAISSSTCreateResponse,
    FAISSSTLoadRequest,
    FAISSSTLoadResponse,
    FAISSSTSearchRequest,
    FAISSSTSearchResponse,
    FAISSSTSearchResult,
    FAISSSTCountResponse
)

from app.services.faiss_st_service import (
    FAISSSTService
)


router = APIRouter(
    prefix="/faiss/st",
    tags=["FAISS - Sentence Transformer"]
)


service = FAISSSTService()


# ==========================================================
# Create IndexFlatL2
# ==========================================================

@router.post(
    "/create-flat-l2",
    response_model=FAISSSTCreateResponse
)
def create_flat_l2():

    response = (
        service.create_flat_l2()
    )

    return FAISSSTCreateResponse(
        **response
    )


# ==========================================================
# FAISS - Sentence Transformer Load
# ==========================================================

@router.post(

    "/load",

    response_model=FAISSSTLoadResponse

)

def load(

    request: FAISSSTLoadRequest

):

    response = service.load_documents(

        collection_name=request.collection_name

    )

    return FAISSSTLoadResponse(

        **response

    )

# ==========================================================
# Search
# ==========================================================

@router.post(
    "/search",
    response_model=FAISSSTSearchResponse
)
def search(
    request: FAISSSTSearchRequest
):

    response = (
        service.search(
            query=request.query,
            top_k=request.top_k
        )
    )

    return FAISSSTSearchResponse(
        query=response["query"],
        total_results=response[
            "total_results"
        ],
        results=[
            FAISSSTSearchResult(
                **item
            )
            for item in response["results"]
        ]
    )


# ==========================================================
# Count
# ==========================================================

@router.get(
    "/count",
    response_model=FAISSSTCountResponse
)
def count():

    response = service.count()

    return FAISSSTCountResponse(
        **response
    )