import json
from datetime import datetime
from pathlib import Path
from typing import Any


AUDIT_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "human_approval_audit.jsonl"
)


def record_audit(
    event: str,
    details: dict[str, Any],
) -> None:
    """Append one event to the audit trail."""

    AUDIT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "details": details,
    }

    with AUDIT_FILE.open(
        "a",
        encoding="utf-8",
    ) as file:

        file.write(
            json.dumps(entry)
            + "\n"
        )