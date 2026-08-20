from pathlib import Path


BASE_DIR = Path("data").resolve()


def _get_safe_path(filename: str) -> Path:
    """
    Return a file path only if it is inside
    the approved data directory.
    """

    file_path = (BASE_DIR / filename).resolve()

    if not str(file_path).startswith(
        str(BASE_DIR)
    ):
        raise ValueError(
            "Access to this file path is not allowed."
        )

    return file_path


def read_file(filename: str) -> dict:
    """
    Read a text file from the approved data directory.
    """

    file_path = _get_safe_path(filename)

    if not file_path.exists():
        return {
            "filename": filename,
            "error": "File not found."
        }

    if not file_path.is_file():
        return {
            "filename": filename,
            "error": "Path is not a file."
        }

    content = file_path.read_text(
        encoding="utf-8"
    )

    return {
        "filename": filename,
        "content": content,
    }


def write_file(
    filename: str,
    content: str,
) -> dict:
    """
    Write a text file inside the approved
    data directory.
    """

    file_path = _get_safe_path(filename)

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return {
        "filename": filename,
        "status": "File written successfully.",
    }