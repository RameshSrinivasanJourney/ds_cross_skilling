from pydantic import BaseModel


# ==========================================================
# FAISS - Index
# ==========================================================

class CreateFlatL2Request(BaseModel):

    dimension: int = 1536


class CreateFlatL2Response(BaseModel):

    status: str

    index_type: str

    dimension: int

    message: str


# ==========================================================
# FAISS - Load
# ==========================================================

class FaissLoadRequest(BaseModel):

    collection_name: str = "employee_documents"


class FaissLoadResponse(BaseModel):

    status: str

    collection_name: str

    total_vectors: int

    message: str


# ==========================================================
# FAISS - Search
# ==========================================================

class FaissSearchRequest(BaseModel):

    query: str

    top_k: int = 3


class FaissSearchResult(BaseModel):

    index: int

    document_id: str

    department: str

    category: str

    text: str

    score: float


class FaissSearchResponse(BaseModel):

    query: str

    total_results: int

    results: list[FaissSearchResult]


# ==========================================================
# FAISS - Count
# ==========================================================

class FaissCountResponse(BaseModel):

    total_vectors: int