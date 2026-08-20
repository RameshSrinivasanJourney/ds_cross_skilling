import logging
from pathlib import Path


LOG_FILE = (
    Path(__file__).resolve().parents[2]
    / "agent_execution.log"
)


def configure_logging() -> logging.Logger:
    """Configure agent execution logging."""

    logger = logging.getLogger(
        "single_agent"
    )

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        console_handler
    )

    return logger