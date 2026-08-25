from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import (
    JSONResponse,
)
from fastapi.middleware.cors import (
    CORSMiddleware,
)

from app.api.routes.chat import (
    router as chat_router,
)
from app.api.routes.jobs import (
    router as jobs_router,
)
from app.api.routes.websocket import (
    router as websocket_router,
)
from app.core.exceptions import (
    LLMServiceError,
)
from app.middleware.security import (
    RateLimitMiddleware,
)

from app.api.routes.sessions import (
    router as session_router,
)

from app.api.routes.files import (
    router as files_router,
)


app = FastAPI(
    title="Module 12 - Production GenAI API",
    version="1.0.0",
)


# --------------------------------------------
# CORS
# --------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------
# Rate limiting
# --------------------------------------------

app.add_middleware(
    RateLimitMiddleware
)


# --------------------------------------------
# Exception handler
# --------------------------------------------

@app.exception_handler(
    LLMServiceError
)
async def llm_exception_handler(
    request: Request,
    exc: LLMServiceError,
):

    return JSONResponse(
        status_code=503,
        content={
            "error": "llm_service_error",
            "message": exc.message,
        },
    )


# --------------------------------------------
# Health
# --------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok"
    }


# --------------------------------------------
# Routes
# --------------------------------------------

app.include_router(
    chat_router
)

app.include_router(
    jobs_router
)

app.include_router(
    websocket_router
)

app.include_router(
    session_router
)

app.include_router(
    files_router
)