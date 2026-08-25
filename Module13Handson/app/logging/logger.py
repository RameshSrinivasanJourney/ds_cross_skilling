import logging
import sys

from app.logging.json_formatter import (
    JsonFormatter,
)


def get_logger(
    name: str = "module13",
) -> logging.Logger:
    """Create/configure a structured logger."""

    logger = logging.getLogger(
        name
    )

    logger.setLevel(
        logging.DEBUG
    )

    if not logger.handlers:

        handler = logging.StreamHandler(
            sys.stdout
        )

        handler.setLevel(
            logging.DEBUG
        )

        handler.setFormatter(
            JsonFormatter()
        )

        logger.addHandler(
            handler
        )

    logger.propagate = False

    return logger