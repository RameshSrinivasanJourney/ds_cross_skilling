from pydantic import BaseModel, Field
from typing import Optional

# ==========================================================
# Health
# ==========================================================

class HealthResponse(BaseModel):

    status: str

    message: str


# ==========================================================
# Common Request / Response Models
# ==========================================================

class ChromaRequest(BaseModel):

    text: str

    document_id: str | None = None


class ChromaResponse(BaseModel):

    status: str

    message: str


# ==========================================================
# Document Search
# ==========================================================

class SearchRequest(BaseModel):

    query: str

    top_k: int = 3


class SearchResult(BaseModel):

    document_id: str

    department: str

    category: str

    text: str

    distance: float


class SearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Delete Documents
# ==========================================================

class DeleteDocumentsRequest(BaseModel):

    document_ids: list[str]


# ==========================================================
# Collections
# ==========================================================

class CollectionListResponse(BaseModel):

    status: str

    total_collections: int

    collections: list[str]


class CollectionInfoRequest(BaseModel):

    collection_name: str


class CollectionInfoResponse(BaseModel):

    status: str

    collection_name: str

    document_count: int


# ==========================================================
# Collection Statistics
# ==========================================================

class DocumentCountResponse(BaseModel):

    status: str

    total_documents: int


# ==========================================================
# Peek Documents
# ==========================================================

class PeekRequest(BaseModel):

    limit: int = Field(

        default=5,

        ge=1,

        le=100

    )


class PeekDocument(BaseModel):

    document_id: str

    department: str

    category: str

    text: str


class PeekResponse(BaseModel):

    status: str

    total_documents: int

    documents: list[PeekDocument]


# ==========================================================
# Embeddings
# ==========================================================

class ChromaEmbeddedResponse(BaseModel):

    status: str

    message: str


# ==========================================================
# Vector Search
# ==========================================================

class VectorSearchRequest(BaseModel):

    query: str

    top_k: int = 3


class VectorSearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Metadata Search
# ==========================================================

class MetadataSearchRequest(BaseModel):

    query: str

    department: Optional[str] = None

    category: Optional[str] = None

    top_k: int = 3


class MetadataSearchResponse(BaseModel):

    query: str

    department: Optional[str] = None

    category: Optional[str] = None

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Storage
# ==========================================================

class MemoryStorageResponse(BaseModel):

    status: str

    storage_type: str

    collection_name: str

    total_documents: int

    message: str