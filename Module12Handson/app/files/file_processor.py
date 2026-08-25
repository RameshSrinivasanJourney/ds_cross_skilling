import json
from pathlib import Path

from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".json",
    ".pdf",
}


def validate_extension(
    filename: str,
) -> str:
    """Validate and return the lowercase extension."""

    extension = (
        Path(filename)
        .suffix
        .lower()
    )

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return extension


def extract_text(
    file_path: Path,
) -> str:
    """Extract text from supported file types."""

    extension = (
        file_path
        .suffix
        .lower()
    )

    if extension == ".txt":

        return file_path.read_text(
            encoding="utf-8"
        )

    if extension == ".json":

        data = json.loads(
            file_path.read_text(
                encoding="utf-8"
            )
        )

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )

    if extension == ".pdf":

        reader = PdfReader(
            str(file_path)
        )

        pages = []

        for page in reader.pages:

            pages.append(
                page.extract_text() or ""
            )

        return "\n".join(
            pages
        )

    raise ValueError(
        f"Unsupported extension: {extension}"
    )