import asyncio
import uuid

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
)

from app.dependencies.common import (
    get_llm_service,
    verify_api_key,
)
from app.models.chat import (
    ChatRequest,
    JobResponse,
)
from app.services.llm_service import (
    LLMService,
)


router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["jobs"],
)


jobs: dict[str, dict] = {}


async def process_job(
    job_id: str,
    question: str,
):

    jobs[job_id]["status"] = "running"

    try:

        llm = LLMService()

        answer = await llm.generate_async(
            question
        )

        jobs[job_id].update(
            {
                "status": "completed",
                "result": answer,
            }
        )

    except Exception as exc:

        jobs[job_id].update(
            {
                "status": "failed",
                "error": str(exc),
            }
        )


@router.post(
    "",
    response_model=JobResponse,
)
async def create_job(
    request: ChatRequest,
    background_tasks: BackgroundTasks,
    _: str = Depends(
        verify_api_key
    ),
):

    job_id = str(
        uuid.uuid4()
    )

    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
    }

    background_tasks.add_task(
        process_job,
        job_id,
        request.question,
    )

    return JobResponse(
        job_id=job_id,
        status="queued",
    )


@router.get(
    "/{job_id}"
)
async def get_job(
    job_id: str,
    _: str = Depends(
        verify_api_key
    ),
):

    return jobs.get(
        job_id,
        {
            "job_id": job_id,
            "status": "not_found",
        },
    )