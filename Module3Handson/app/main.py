from fastapi import FastAPI
from app.api.chat_api import chat_router
from app.utils.logger import logger
from app.api.prompt_api import prompt_router

logger.info("Application Started Successfully")

app = FastAPI(
    title="Module3Handson"
)

app.include_router(chat_router)
app.include_router(prompt_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Module3Handson API",
        "docs": "/docs"
    }