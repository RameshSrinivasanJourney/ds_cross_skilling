from pydantic import BaseModel, Field
from typing import Optional


# ==========================================================
# Qdrant - Health
# ==========================================================

class QdrantHealthResponse(BaseModel):

    status: str

    message: str

    total_collections: int


# ==========================================================
# Qdrant - Collections
# ==========================================================

class CreateCollectionRequest(BaseModel):

    collection_name: str

    vector_size: int = 1536

    distance: str = "Cosine"


class CreateCollectionResponse(BaseModel):

    status: str

    collection_name: str

    vector_size: int

    distance: str

    message: str


class CollectionListResponse(BaseModel):

    status: str

    total_collections: int

    collections: list[str]


class CollectionInfoRequest(BaseModel):

    collection_name: str


class CollectionInfoResponse(BaseModel):

    status: str

    collection_name: str

    total_points: int

    vector_size: int


class DeleteCollectionRequest(BaseModel):

    collection_name: str


class DeleteCollectionResponse(BaseModel):

    status: str

    message: str


# ==========================================================
# Qdrant - Points
# ==========================================================

class LoadPointsResponse(BaseModel):

    status: str

    collection_name: str

    total_points: int

    message: str


class PointCountResponse(BaseModel):

    status: str

    collection_name: str

    total_points: int


class DeletePointRequest(BaseModel):

    collection_name: str

    point_id: int


class DeletePointResponse(BaseModel):

    status: str

    message: str


# ==========================================================
# Qdrant - Search / Dense Search
# ==========================================================

class SearchRequest(BaseModel):

    collection_name: str

    query: str

    top_k: int = 3


class SearchResult(BaseModel):

    point_id: str

    department: str

    category: str

    text: str

    score: float

    hybrid_score: float | None = None


class SearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Qdrant - Payload Filtering
# ==========================================================

class PayloadFilterRequest(BaseModel):

    collection_name: str

    query: str

    department: Optional[str] = None

    category: Optional[str] = None

    top_k: int = 3


class PayloadFilterResponse(BaseModel):

    query: str

    department: Optional[str] = None

    category: Optional[str] = None

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Qdrant - Hybrid Search
# ==========================================================

class HybridSearchRequest(BaseModel):

    collection_name: str

    query: str

    top_k: int = 3


class HybridSearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[SearchResult]


# ==========================================================
# Qdrant - Named Vectors
# ==========================================================

class NamedVectorLoadResponse(BaseModel):

    status: str

    collection_name: str

    total_points: int

    message: str


class NamedVectorSearchRequest(BaseModel):

    collection_name: str

    query: str

    vector_name: str = "text"

    top_k: int = 3


class NamedVectorSearchResponse(BaseModel):

    query: str

    vector_name: str

    total_results: int

    results: list[SearchResult]

# ==========================================================
# Qdrant - Named Vector Collection
# ==========================================================

class NamedVectorCollectionRequest(BaseModel):

    collection_name: str

 
class NamedVectorCollectionResponse(BaseModel):

    status: str

    collection_name: str

    vector_names: list[str]

    vector_size: int

    message: str

# ==========================================================
# Qdrant - Named Vector Load
# ==========================================================

class NamedVectorLoadRequest(BaseModel):

    collection_name: str


class NamedVectorLoadResponse(BaseModel):

    status: str

    collection_name: str

    total_points: int

    message: str

# ==========================================================
# Qdrant - Named Vector Search
# ==========================================================

class NamedVectorSearchRequest(BaseModel):

    collection_name: str

    query: str

    vector_name: str = "text"

    top_k: int = 3


class NamedVectorSearchResponse(BaseModel):

    query: str

    vector_name: str

    total_results: int

    results: list[SearchResult]