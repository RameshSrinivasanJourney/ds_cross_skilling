from fastapi import FastAPI

from app.api.indexing_api import router as indexing_router
from app.api.rag_api import router as rag_router
from app.api.advanced_retrieval_api import router as multi_query_router
from app.api.generation_api import router as generation_router
from app.api.evaluation_api import router as evaluation_router

app = FastAPI(
    title="Module 6 - RAG",
    description="Retrieval-Augmented Generation learning project",
    version="1.0.0"
)

app.include_router(
    indexing_router
)

app.include_router(
    rag_router
)

app.include_router(
    multi_query_router
)

app.include_router(
    generation_router
)

app.include_router(
    evaluation_router
)

@app.get("/")
def root():

    return {
        "status": "Success",
        "module": "Module 6",
        "topic": "RAG Architecture"
    }