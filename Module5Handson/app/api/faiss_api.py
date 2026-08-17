from fastapi import APIRouter

from app.models.faiss_models import (
    CreateFlatL2Request,
    CreateFlatL2Response,
    FaissLoadRequest,
    FaissLoadResponse,
    FaissSearchRequest,
    FaissSearchResponse,
    FaissSearchResult,
    FaissCountResponse
)

from app.services.faiss_service import FaissService


router = APIRouter(

    prefix="/faiss",

    tags=["FAISS"]

)


service = FaissService()


# ==========================================================
# FAISS - Create IndexFlatL2
# ==========================================================

@router.post(

    "/index/create-flat-l2",

    response_model=CreateFlatL2Response

)

def create_flat_l2(

    request: CreateFlatL2Request

):

    response = service.create_flat_l2(

        dimension=request.dimension

    )

    return CreateFlatL2Response(

        **response

    )


# ==========================================================
# FAISS - Load
# ==========================================================

@router.post(

    "/load",

    response_model=FaissLoadResponse

)

def load(

    request: FaissLoadRequest

):

    response = service.load(

        collection_name=request.collection_name

    )

    return FaissLoadResponse(

        **response

    )


# ==========================================================
# FAISS - Search
# ==========================================================

@router.post(

    "/search",

    response_model=FaissSearchResponse

)

def search(

    request: FaissSearchRequest

):

    response = service.search(

        query=request.query,

        top_k=request.top_k

    )

    return FaissSearchResponse(

        query=response["query"],

        total_results=response["total_results"],

        results=[

            FaissSearchResult(

                **item

            )

            for item in response["results"]

        ]

    )


# ==========================================================
# FAISS - Count
# ==========================================================

@router.get(

    "/count",

    response_model=FaissCountResponse

)

def count():

    return FaissCountResponse(

        total_vectors=service.count()

    )