from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from typing import Any
import json


@dataclass
class MemoryRecord:
    """Metadata associated with one vector memory."""

    memory_id: int
    memory_type: str
    text: str
    user_id: str
    created_at: str
    expires_at: str | None = None
    importance: float = 1.0

    def is_expired(self) -> bool:
        """Return True when the memory has expired."""

        if self.expires_at is None:
            return False

        expiry = datetime.fromisoformat(
            self.expires_at
        )

        return datetime.now() >= expiry

    def freshness(self) -> float:
        """Return a simple freshness score."""

        created = datetime.fromisoformat(
            self.created_at
        )

        age_hours = (
            datetime.now() - created
        ).total_seconds() / 3600

        return 1.0 / (
            1.0 + max(age_hours, 0.0)
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)