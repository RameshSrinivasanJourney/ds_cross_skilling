from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    File,
    HTTPException,
    UploadFile,
    status,
)

from app.dependencies.common import (
    verify_api_key,
)
from app.files.file_jobs import (
    create_job,
    get_job,
    update_job,
)
from app.files.file_service import (
    FileService,
)
from app.models.file import (
    FileJobStatus,
    FileUploadResponse,
)


router = APIRouter(
    prefix="/api/v1/files",
    tags=["files"],
)


async def process_file_background(
    job_id: str,
    file_path,
):

    update_job(
        job_id,
        status="processing",
    )

    service = FileService()

    try:

        result = await service.process_file(
            file_path
        )

        update_job(
            job_id,
            status="completed",
            result=result,
        )

    except Exception as exc:

        if file_path.exists():
            file_path.unlink()

        update_job(
            job_id,
            status="failed",
            error=str(exc),
        )


@router.post(
    "/upload",
    response_model=FileUploadResponse,
)
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    _: str = Depends(
        verify_api_key
    ),
):

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is required.",
        )

    service = FileService()

    try:

        job_id, file_path = (
            await service.save_upload(
                file
            )
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    create_job(
        job_id,
        file.filename,
    )

    background_tasks.add_task(
        process_file_background,
        job_id,
        file_path,
    )

    return FileUploadResponse(
        job_id=job_id,
        filename=file.filename,
        status="queued",
    )


@router.get(
    "/{job_id}",
    response_model=FileJobStatus,
)
async def get_file_job(
    job_id: str,
    _: str = Depends(
        verify_api_key
    ),
):

    job = get_job(
        job_id
    )

    if job is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File job not found.",
        )

    return job