import hashlib
import time
from dataclasses import dataclass


@dataclass
class CacheEntry:
    response: str
    created_at: float
    input_tokens: int
    output_tokens: int


class ExactCache:
    """Simple exact-match cache for Topic 1."""

    def __init__(self):

        self._cache: dict[
            str,
            CacheEntry,
        ] = {}

    @staticmethod
    def _key(
        prompt: str,
    ) -> str:

        normalized = (
            prompt.strip()
            .lower()
        )

        return hashlib.sha256(
            normalized.encode(
                "utf-8"
            )
        ).hexdigest()

    def get(
        self,
        prompt: str,
    ) -> CacheEntry | None:

        key = self._key(
            prompt
        )

        return self._cache.get(
            key
        )

    def set(
        self,
        prompt: str,
        response: str,
        input_tokens: int,
        output_tokens: int,
    ) -> None:

        key = self._key(
            prompt
        )

        self._cache[key] = CacheEntry(
            response=response,
            created_at=time.time(),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )