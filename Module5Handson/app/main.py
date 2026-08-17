from fastapi import FastAPI

from app.api.chroma_api import chroma_router
from app.api.qdrant_api import qdrant_router
from app.api.faiss_api import router as faiss_router
from app.api.faiss_st_api import router as faiss_st_router


app = FastAPI(

    title="Module 5 - ChromaDB",

    version="1.0.0"

)


app.include_router(

    chroma_router

)

app.include_router(

    qdrant_router
    
)

app.include_router(

    faiss_router

)

app.include_router(

    faiss_st_router

)