import asyncio
import shutil
import uuid
from pathlib import Path

from app.files.file_processor import (
    extract_text,
    validate_extension,
)
from app.services.llm_service import (
    LLMService,
)


UPLOAD_DIR = Path("uploads")
TEMP_DIR = Path("temp")

MAX_FILE_SIZE = 5 * 1024 * 1024


class FileService:
    """Handle temporary file storage and processing."""

    def __init__(self):

        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        TEMP_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def save_upload(
        self,
        upload_file,
    ) -> tuple[str, Path]:

        validate_extension(
            upload_file.filename
        )

        job_id = str(
            uuid.uuid4()
        )

        safe_filename = (
            Path(
                upload_file.filename
            ).name
        )

        temp_path = (
            TEMP_DIR
            / f"{job_id}_{safe_filename}"
        )

        total_size = 0

        try:

            with temp_path.open(
                "wb"
            ) as output:

                while True:

                    chunk = (
                        await upload_file.read(
                            1024 * 1024
                        )
                    )

                    if not chunk:
                        break

                    total_size += len(
                        chunk
                    )

                    if (
                        total_size
                        > MAX_FILE_SIZE
                    ):

                        raise ValueError(
                            "File exceeds the "
                            "5 MB size limit."
                        )

                    output.write(chunk)

        except Exception:

            if temp_path.exists():
                temp_path.unlink()

            raise

        finally:

            await upload_file.close()

        return job_id, temp_path

    async def process_file(
        self,
        file_path: Path,
    ) -> str:

        try:

            text = await asyncio.to_thread(
                extract_text,
                file_path,
            )

            if not text.strip():

                return (
                    "File processed successfully, "
                    "but no extractable text was found."
                )

            llm = LLMService()

            prompt = (
                "Summarize the following uploaded "
                "document in a concise way.\n\n"
                f"{text[:12000]}"
            )

            summary = (
                await llm.generate_async(
                    prompt
                )
            )

            return summary

        finally:

            if file_path.exists():
                file_path.unlink()

    async def cleanup_temp_files(
        self,
    ) -> int:

        removed = 0

        for path in TEMP_DIR.iterdir():

            if path.is_file():

                try:

                    path.unlink()
                    removed += 1

                except OSError:

                    pass

        return removed