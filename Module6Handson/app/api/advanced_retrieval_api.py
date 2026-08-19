from fastapi import APIRouter

from app.models.advanced_retrieval_models import (
    MultiQueryRequest,
    MultiQueryResponse,
    MultiQueryResult,
    QueryRetrievalResult
)

from app.services.multi_query_service import (
    MultiQueryService
)


router = APIRouter(
    prefix="/rag",
    tags=["Advanced Retrieval"]
)


# ==========================================================
# Multi-Query Retrieval
# ==========================================================

@router.post(
    "/multi-query",
    response_model=MultiQueryResponse
)
def multi_query_retrieve(
    request: MultiQueryRequest
):

    response = (
        MultiQueryService.retrieve(
            query=request.query,
            top_k=request.top_k
        )
    )

    return MultiQueryResponse(

        original_query=
            response["original_query"],

        generated_queries=
            response["generated_queries"],

        query_results=[
            QueryRetrievalResult(

                query=item["query"],

                results=[
                    MultiQueryResult(
                        **result
                    )
                    for result
                    in item["results"]
                ]
            )

            for item
            in response["query_results"]
        ],

        total_results=
            response["total_results"],

        results=[
            MultiQueryResult(
                **result
            )
            for result
            in response["results"]
        ],

        context=
            response["context"]
    )