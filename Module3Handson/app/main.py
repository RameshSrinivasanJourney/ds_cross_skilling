from fastapi import FastAPI
from app.api.chat_api import router
from app.utils.logger import logger

logger.info("Application Started Successfully")

app = FastAPI(
    title="Module2Handson"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Module2Handson API",
        "docs": "/docs"
    }