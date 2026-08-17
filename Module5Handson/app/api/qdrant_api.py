from fastapi import APIRouter

from app.models.qdrant_models import (

    QdrantHealthResponse,

    CreateCollectionRequest,
    CreateCollectionResponse,

    CollectionListResponse,

    CollectionInfoRequest,
    CollectionInfoResponse,

    DeleteCollectionRequest,
    DeleteCollectionResponse,

    LoadPointsResponse,
    PointCountResponse,
    DeletePointRequest,
    DeletePointResponse,

    SearchRequest,
    SearchResponse,
    SearchResult,

    PayloadFilterRequest,
    PayloadFilterResponse,

    HybridSearchRequest,
    HybridSearchResponse,

    NamedVectorCollectionRequest,
    NamedVectorCollectionResponse,

    NamedVectorLoadRequest,
    NamedVectorLoadResponse,

    NamedVectorSearchRequest,
    NamedVectorSearchResponse

)

from app.services.qdrant_service import QdrantService


qdrant_router = APIRouter(

    prefix="/qdrant"

)

service = QdrantService()


# ==========================================================
# Qdrant - Health
# ==========================================================

@qdrant_router.get(

    "/health",

    tags=["Qdrant - Health"],

    response_model=QdrantHealthResponse

)
def health():

    response = service.health()

    return QdrantHealthResponse(

        status=response["status"],

        message=response["message"],

        total_collections=response["total_collections"]

    )


# ==========================================================
# Qdrant - Collections
# ==========================================================

@qdrant_router.post(

    "/collection/create",

    tags=["Qdrant - Collections"],

    response_model=CreateCollectionResponse

)
def create_collection(

    request: CreateCollectionRequest

):

    response = service.create_collection(

        collection_name=request.collection_name,

        vector_size=request.vector_size,

        distance=request.distance

    )

    return CreateCollectionResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        vector_size=response["vector_size"],

        distance=response["distance"],

        message=response["message"]

    )


@qdrant_router.get(

    "/collections",

    tags=["Qdrant - Collections"],

    response_model=CollectionListResponse

)
def list_collections():

    response = service.list_collections()

    return CollectionListResponse(

        status=response["status"],

        total_collections=response["total_collections"],

        collections=response["collections"]

    )


@qdrant_router.post(

    "/collection/info",

    tags=["Qdrant - Collections"],

    response_model=CollectionInfoResponse

)
def collection_info(

    request: CollectionInfoRequest

):

    response = service.collection_info(

        collection_name=request.collection_name

    )

    return CollectionInfoResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        total_points=response["total_points"],

        vector_size=response["vector_size"]

    )


@qdrant_router.delete(

    "/collection/delete",

    tags=["Qdrant - Collections"],

    response_model=DeleteCollectionResponse

)
def delete_collection(

    request: DeleteCollectionRequest

):

    response = service.delete_collection(

        collection_name=request.collection_name

    )

    return DeleteCollectionResponse(

        status=response["status"],

        message=response["message"]

    )

# ==========================================================
# Qdrant - Points
# ==========================================================

@qdrant_router.post(

    "/points/load",

    tags=["Qdrant - Points"],

    response_model=LoadPointsResponse

)
def load_points(

    collection_name: str

):

    response = service.load_points(

        collection_name=collection_name

    )

    return LoadPointsResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        total_points=response["total_points"],

        message=response["message"]

    )


@qdrant_router.get(

    "/points/count",

    tags=["Qdrant - Points"],

    response_model=PointCountResponse

)
def point_count(

    collection_name: str

):

    response = service.point_count(

        collection_name=collection_name

    )

    return PointCountResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        total_points=response["total_points"]

    )


@qdrant_router.delete(

    "/point/delete",

    tags=["Qdrant - Points"],

    response_model=DeletePointResponse

)
def delete_point(

    request: DeletePointRequest

):

    response = service.delete_point(

        collection_name=request.collection_name,

        point_id=request.point_id

    )

    return DeletePointResponse(

        status=response["status"],

        message=response["message"]

    )

# ==========================================================
# Qdrant - Search / dense search
# ==========================================================

@qdrant_router.post(

    "/dense-search",

    tags=["Qdrant - Search"],

    response_model=SearchResponse

)
def search(

    request: SearchRequest

):

    response = service.search(

        collection_name=request.collection_name,

        query=request.query,

        top_k=request.top_k

    )

    return SearchResponse(

        query=response["query"],

        total_results=response["total_results"],

        results=[

            SearchResult(**item)

            for item in response["results"]

        ]

    )

# ==========================================================
# Qdrant - Payload Filtering
# ==========================================================

@qdrant_router.post(

    "/payload-search",

    tags=["Qdrant - Payload Filtering"],

    response_model=PayloadFilterResponse

)
def payload_search(

    request: PayloadFilterRequest

):

    response = service.payload_search(

        collection_name=request.collection_name,

        query=request.query,

        department=request.department,

        category=request.category,

        top_k=request.top_k

    )

    return PayloadFilterResponse(

        query=response["query"],

        department=response["department"],

        category=response["category"],

        total_results=response["total_results"],

        results=[

            SearchResult(**item)

            for item in response["results"]

        ]

    )

# ==========================================================
# Qdrant - Keyword Search
# ==========================================================

@qdrant_router.post(

    "/keyword-search",

    tags=["Qdrant - Search"]

)

def keyword_search(

    request: SearchRequest

):

    return service.keyword_search(

        collection_name=request.collection_name,

        query=request.query,

        top_k=request.top_k

    )

@qdrant_router.post(

    "/hybrid-search",
    tags=["Qdrant - Search"]
)

def hybrid_search(

    request: HybridSearchRequest

):

    response = service.hybrid_search(

        collection_name=request.collection_name,

        query=request.query,

        top_k=request.top_k

    )

    return HybridSearchResponse(

        query=response["query"],

        total_results=response["total_results"],

        results=[

            SearchResult(**item)

            for item in response["results"]

        ]

    )

# ==========================================================
# Qdrant - Named Vector Collection
# ==========================================================

@qdrant_router.post(

    "/named-vectors/create-collection",

    response_model=NamedVectorCollectionResponse,

    tags=["Qdrant - Named Vectors"]

)

def create_named_vector_collection(

    request: NamedVectorCollectionRequest

):

    response = service.create_named_vector_collection(

        collection_name=request.collection_name

    )

    return NamedVectorCollectionResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        vector_names=response["vector_names"],

        vector_size=response["vector_size"],

        message=response["message"]

    )

# ==========================================================
# Qdrant - Named Vector Load
# ==========================================================

@qdrant_router.post(

    "/named-vectors/load",

    response_model=NamedVectorLoadResponse,

    tags=["Qdrant - Named Vectors"]

)

def load_named_vectors(

    request: NamedVectorLoadRequest

):

    response = service.load_named_vectors(

        collection_name=request.collection_name

    )

    return NamedVectorLoadResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        total_points=response["total_points"],

        message=response["message"]

    )

# ==========================================================
# Qdrant - Named Vector Search
# ==========================================================

@qdrant_router.post(

    "/named-vectors/search",

    response_model=NamedVectorSearchResponse,

    tags=["Qdrant - Named Vectors"]

)

def named_vector_search(

    request: NamedVectorSearchRequest

):

    response = service.named_vector_search(

        collection_name=request.collection_name,

        query=request.query,

        vector_name=request.vector_name,

        top_k=request.top_k

    )

    return NamedVectorSearchResponse(

        query=response["query"],

        vector_name=response["vector_name"],

        total_results=response["total_results"],

        results=[

            SearchResult(**item)

            for item in response["results"]

        ]

    )