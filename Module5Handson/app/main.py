from fastapi import FastAPI

from app.api.chroma_api import chroma_router


app = FastAPI(

    title="Module 5 - ChromaDB",

    version="1.0.0"

)


app.include_router(

    chroma_router

)