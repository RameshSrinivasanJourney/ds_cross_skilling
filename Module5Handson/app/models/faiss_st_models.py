from pydantic import BaseModel


# ==========================================================
# Create
# ==========================================================

class FAISSSTCreateResponse(BaseModel):

    status: str

    dimension: int

    index_type: str

    message: str


# ==========================================================
# Load
# ==========================================================

class FAISSSTLoadRequest(BaseModel):

    collection_name: str


class FAISSSTLoadResponse(BaseModel):

    status: str

    total_documents: int

    dimension: int

    message: str


# ==========================================================
# Search
# ==========================================================

class FAISSSTSearchRequest(BaseModel):

    query: str

    top_k: int = 3


class FAISSSTSearchResult(BaseModel):

    point_id: str

    department: str

    category: str

    text: str

    distance: float


class FAISSSTSearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[
        FAISSSTSearchResult
    ]


# ==========================================================
# Count
# ==========================================================

class FAISSSTCountResponse(BaseModel):

    status: str

    total_vectors: int