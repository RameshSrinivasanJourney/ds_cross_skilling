import json
import logging
from datetime import datetime, timezone
from typing import Any

from app.logging.pii_scrubber import (
    scrub_pii,
)


class JsonFormatter(
    logging.Formatter
):
    """Convert log records into JSON."""

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:

        payload: dict[str, Any] = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "service": "module13",
            "message": scrub_pii(
                record.getMessage()
            ),
        }

        context = getattr(
            record,
            "context",
            None,
        )

        if isinstance(
            context,
            dict,
        ):

            cleaned_context = {}

            for key, value in (
                context.items()
            ):

                if isinstance(
                    value,
                    str,
                ):

                    cleaned_context[
                        key
                    ] = scrub_pii(
                        value
                    )

                else:

                    cleaned_context[
                        key
                    ] = value

            payload[
                "context"
            ] = cleaned_context

        return json.dumps(
            payload,
            ensure_ascii=False,
        )