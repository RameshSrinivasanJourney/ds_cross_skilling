from fastapi import APIRouter

from app.models.chroma_models import (
    HealthResponse,
    ChromaResponse,
    SearchRequest,
    SearchResponse,
    SearchResult,
    DeleteDocumentsRequest,
    CollectionListResponse,
    CollectionInfoRequest,
    CollectionInfoResponse,
    DocumentCountResponse,
    PeekRequest,
    PeekResponse,
    PeekDocument,
    ChromaEmbeddedResponse,
    VectorSearchRequest,
    VectorSearchResponse,
    MetadataSearchRequest,
    MetadataSearchResponse,
    MemoryStorageResponse
)

from app.services.chroma_service import ChromaService


chroma_router = APIRouter(
    prefix="/chroma"
)

service = ChromaService()


# ==========================================================
# Health
# ==========================================================

@chroma_router.get(
    "/health",
    tags=["ChromaDB - Health"],
    response_model=HealthResponse
)
def health():

    return HealthResponse(

        status="Success",

        message=service.health()

    )


# ==========================================================
# Document Management
# ==========================================================

@chroma_router.post(
    "/load",
    tags=["ChromaDB - Documents"],
    response_model=ChromaResponse
)
def load_documents():

    response = service.load_documents()

    return ChromaResponse(

        status=response["status"],

        message=response["message"]

    )

@chroma_router.delete(
    "/document/{document_id}",
    tags=["ChromaDB - Documents"],
    response_model=ChromaResponse
)
def delete_document(document_id: str):

    response = service.delete_document(document_id)

    return ChromaResponse(

        status=response["status"],

        message=response["message"]

    )

@chroma_router.delete(
    "/documents",
    tags=["ChromaDB - Documents"],
    response_model=ChromaResponse
)
def delete_documents(request: DeleteDocumentsRequest):

    response = service.delete_documents(

        request.document_ids

    )

    return ChromaResponse(

        status=response["status"],

        message=response["message"]

    )

@chroma_router.delete(
    "/documents/all",
    tags=["ChromaDB - Documents"],
    response_model=ChromaResponse
)
def delete_all_documents():

    response = service.delete_all_documents()

    return ChromaResponse(

        status=response["status"],

        message=response["message"]

    )

# ==========================================================
# Collection Management
# ==========================================================

@chroma_router.get(
    "/collections",
    tags=["ChromaDB - Collections"],
    response_model=CollectionListResponse
)
def list_collections():

    response = service.list_collections()

    return CollectionListResponse(

        status=response["status"],

        total_collections=response["total_collections"],

        collections=response["collections"]

    )

@chroma_router.post(
    "/collection-info",
    tags=["ChromaDB - Collections"],
    response_model=CollectionInfoResponse
)
def collection_info(request: CollectionInfoRequest):

    response = service.collection_info(

        collection_name=request.collection_name

    )

    return CollectionInfoResponse(

        status=response["status"],

        collection_name=response["collection_name"],

        document_count=response["document_count"]

    )

@chroma_router.get(
    "/count",
    tags=["ChromaDB - Collections"],
    response_model=DocumentCountResponse
)
def document_count():

    response = service.document_count()

    return DocumentCountResponse(

        status=response["status"],

        total_documents=response["total_documents"]

    )

@chroma_router.post(
    "/peek",
    tags=["ChromaDB - Collections"],
    response_model=PeekResponse
)
def peek_documents(request: PeekRequest):

    response = service.peek_documents(

        limit=request.limit

    )

    return PeekResponse(

        status=response["status"],

        total_documents=response["total_documents"],

        documents=[

            PeekDocument(**item)

            for item in response["documents"]

        ]

    )

# ==========================================================
# Embedding Management
# ==========================================================

@chroma_router.post(
    "/load-embeddings",
    tags=["ChromaDB - Embeddings"],
    response_model=ChromaEmbeddedResponse
)
def load_embedded_documents():

    response = service.load_embedded_documents()

    return ChromaEmbeddedResponse(

        status=response["status"],

        message=response["message"]

    )

# ==========================================================
# Search
# ==========================================================

@chroma_router.post(
    "/search",
    tags=["ChromaDB - Search"],
    response_model=SearchResponse
)
def search_documents(request: SearchRequest):

    response = service.search_documents(

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

@chroma_router.post(
    "/vector-search",
    tags=["ChromaDB - Search"],
    response_model=VectorSearchResponse
)
def vector_search(request: VectorSearchRequest):

    response = service.vector_search(

        query=request.query,

        top_k=request.top_k

    )

    return VectorSearchResponse(

        query=response["query"],

        total_results=response["total_results"],

        results=[

            SearchResult(**item)

            for item in response["results"]

        ]

    )

# ==========================================================
# Metadata Filtering
# ==========================================================

@chroma_router.post(

    "/metadata-search",

    tags=["ChromaDB - Metadata Filtering"],

    response_model=MetadataSearchResponse

)
def metadata_search(

    request: MetadataSearchRequest

):

    response = service.metadata_search(

        query=request.query,

        department=request.department,

        category=request.category,

        top_k=request.top_k

    )

    return MetadataSearchResponse(

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
# Storage
# ==========================================================

@chroma_router.post(

    "/memory-demo",

    tags=["ChromaDB - Storage"],

    response_model=MemoryStorageResponse

)
def memory_demo():

    response = service.memory_demo()

    return MemoryStorageResponse(

        status=response["status"],

        storage_type=response["storage_type"],

        collection_name=response["collection_name"],

        total_documents=response["total_documents"],

        message=response["message"]

    )
