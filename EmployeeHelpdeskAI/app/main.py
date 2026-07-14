from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.home import router as home_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="Employee Helpdesk AI",
    description="Generative AI Learning Lab",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(home_router)
app.include_router(chat_router)