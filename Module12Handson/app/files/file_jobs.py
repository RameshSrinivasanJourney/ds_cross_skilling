from typing import Any


file_jobs: dict[str, dict[str, Any]] = {}


def create_job(
    job_id: str,
    filename: str,
) -> None:
    """Create a new file-processing job."""

    file_jobs[job_id] = {
        "job_id": job_id,
        "filename": filename,
        "status": "queued",
        "result": None,
        "error": None,
    }


def update_job(
    job_id: str,
    **updates: Any,
) -> None:
    """Update an existing file-processing job."""

    if job_id in file_jobs:
        file_jobs[job_id].update(
            updates
        )


def get_job(
    job_id: str,
) -> dict[str, Any] | None:
    """Retrieve a file-processing job."""

    return file_jobs.get(job_id)