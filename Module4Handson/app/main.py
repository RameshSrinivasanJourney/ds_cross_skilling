from fastapi import FastAPI

from app.api.embedding_api import embedding_router

from app.api.search_api import search_router

from app.api.faiss_api import faiss_router

from app.api.hybrid_search_api import hybrid_router


app = FastAPI(
    title="Module 4 - Embeddings"
)


app.include_router(
    embedding_router
)

app.include_router(
    search_router
)

app.include_router(
    faiss_router
)

app.include_router(
    hybrid_router
)