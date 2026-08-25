import json
import logging
import sys
from typing import Any


class JsonFormatter(
    logging.Formatter
):
    """Format log records as JSON."""

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:

        payload: dict[str, Any] = {
            "timestamp": self.formatTime(
                record,
                "%Y-%m-%dT%H:%M:%S",
            ),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        observation = getattr(
            record,
            "observation",
            None,
        )

        if observation is not None:
            payload["observation"] = observation

        return json.dumps(
            payload,
            ensure_ascii=False,
        )


def configure_logging() -> logging.Logger:
    """Configure structured console logging."""

    logger = logging.getLogger(
        "module13"
    )

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        handler = logging.StreamHandler(
            sys.stdout
        )

        handler.setFormatter(
            JsonFormatter()
        )

        logger.addHandler(
            handler
        )

    logger.propagate = False

    return logger