import asyncio
import json
import uuid
from datetime import datetime
from typing import AsyncGenerator

from fastapi import (
    APIRouter,
    BackgroundTasks,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.responses import (
    StreamingResponse,
)
from ollama import chat


router = APIRouter()

MODEL_NAME = "llama3.2:3b"


# -------------------------------------------------
# In-memory job store for this learning exercise
# -------------------------------------------------

jobs: dict[str, dict] = {}


# -------------------------------------------------
# Helper: Ollama non-streaming call
# -------------------------------------------------

def generate_answer(
    question: str,
) -> str:
    """Generate a complete response."""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )

    return response.message.content


# -------------------------------------------------
# Helper: Ollama streaming call
# -------------------------------------------------

def generate_stream(
    question: str,
):
    """Generate response chunks from Ollama."""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        stream=True,
    )

    for chunk in response:

        content = (
            chunk.message.content
        )

        if content:
            yield content


# -------------------------------------------------
# 1.1 SYNC ENDPOINT
# -------------------------------------------------

@router.post("/chat/sync")
def chat_sync(
    question: str,
):
    """
    Synchronous request/response endpoint.
    """

    answer = generate_answer(
        question
    )

    return {
        "mode": "sync",
        "question": question,
        "answer": answer,
    }


# -------------------------------------------------
# 1.1 ASYNC ENDPOINT
# -------------------------------------------------

@router.post("/chat/async")
async def chat_async(
    question: str,
):
    """
    Async endpoint.

    The Ollama SDK call itself is synchronous,
    so it is moved to a worker thread.
    """

    answer = await asyncio.to_thread(
        generate_answer,
        question,
    )

    return {
        "mode": "async",
        "question": question,
        "answer": answer,
    }


# -------------------------------------------------
# 1.2 STREAMING ENDPOINT
# -------------------------------------------------

@router.post("/chat/stream")
def chat_stream(
    question: str,
):
    """
    Stream generated chunks as plain text.
    """

    return StreamingResponse(
        generate_stream(question),
        media_type="text/plain",
    )


# -------------------------------------------------
# 1.5 SSE ENDPOINT
# -------------------------------------------------

async def sse_generator(
    question: str,
) -> AsyncGenerator[str, None]:

    for chunk in generate_stream(
        question
    ):

        payload = {
            "type": "token",
            "content": chunk,
        }

        yield (
            "data: "
            + json.dumps(payload)
            + "\n\n"
        )

        await asyncio.sleep(0)

    yield (
        "data: "
        + json.dumps(
            {
                "type": "done"
            }
        )
        + "\n\n"
    )


@router.get("/chat/sse")
async def chat_sse(
    question: str,
):
    """
    Server-Sent Events endpoint.
    """

    return StreamingResponse(
        sse_generator(question),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


# -------------------------------------------------
# 1.3 WEBSOCKET
# -------------------------------------------------

@router.websocket("/ws/chat")
async def websocket_chat(
    websocket: WebSocket,
):
    """
    Bidirectional WebSocket chat endpoint.
    """

    await websocket.accept()

    try:

        while True:

            question = (
                await websocket.receive_text()
            )

            await websocket.send_json(
                {
                    "type": "status",
                    "message": "Generating response...",
                }
            )

            answer = await asyncio.to_thread(
                generate_answer,
                question,
            )

            await websocket.send_json(
                {
                    "type": "answer",
                    "content": answer,
                }
            )

    except WebSocketDisconnect:

        print(
            "WebSocket client disconnected."
        )


# -------------------------------------------------
# 1.4 BACKGROUND JOB
# -------------------------------------------------

def process_background_job(
    job_id: str,
    question: str,
) -> None:
    """Execute a long-running background job."""

    jobs[job_id]["status"] = "running"

    try:

        # Simulate background work.
        time_to_wait = 2

        asyncio.run(
            asyncio.sleep(
                time_to_wait
            )
        )

        answer = generate_answer(
            question
        )

        jobs[job_id].update(
            {
                "status": "completed",
                "result": answer,
                "completed_at": (
                    datetime.now().isoformat()
                ),
            }
        )

    except Exception as exc:

        jobs[job_id].update(
            {
                "status": "failed",
                "error": str(exc),
            }
        )


@router.post("/jobs")
def create_job(
    question: str,
    background_tasks: BackgroundTasks,
):
    """
    Start a background job and immediately return
    a job identifier.
    """

    job_id = str(
        uuid.uuid4()
    )

    jobs[job_id] = {
        "job_id": job_id,
        "question": question,
        "status": "queued",
        "created_at": (
            datetime.now().isoformat()
        ),
    }

    background_tasks.add_task(
        process_background_job,
        job_id,
        question,
    )

    return {
        "job_id": job_id,
        "status": "queued",
    }


@router.get("/jobs/{job_id}")
def get_job_status(
    job_id: str,
):
    """
    Poll the current status of a background job.
    """

    job = jobs.get(
        job_id
    )

    if job is None:

        return {
            "job_id": job_id,
            "status": "not_found",
        }

    return job