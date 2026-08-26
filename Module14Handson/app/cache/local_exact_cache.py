import hashlib
import time
from dataclasses import dataclass


@dataclass
class LocalCacheEntry:
    response: str
    model: str
    created_at: float
    expires_at: float
    input_tokens: int
    output_tokens: int


class LocalExactCache:
    """Local exact cache used when Redis isn't available."""

    def __init__(
        self,
        ttl_seconds: int = 300,
    ) -> None:

        self.ttl_seconds = ttl_seconds

        self._cache: dict[
            str,
            LocalCacheEntry,
        ] = {}

    @staticmethod
    def normalize_prompt(
        prompt: str,
    ) -> str:

        return " ".join(
            prompt.strip().lower().split()
        )

    def build_key(
        self,
        prompt: str,
        model: str,
    ) -> str:

        material = (
            f"{model}:"
            f"{self.normalize_prompt(prompt)}"
        )

        return hashlib.sha256(
            material.encode(
                "utf-8"
            )
        ).hexdigest()

    def get(
        self,
        prompt: str,
        model: str,
    ) -> LocalCacheEntry | None:

        key = self.build_key(
            prompt,
            model,
        )

        entry = self._cache.get(
            key
        )

        if entry is None:
            return None

        if time.time() >= entry.expires_at:

            del self._cache[key]

            return None

        return entry

    def set(
        self,
        prompt: str,
        model: str,
        response: str,
        input_tokens: int,
        output_tokens: int,
    ) -> None:

        now = time.time()

        key = self.build_key(
            prompt,
            model,
        )

        self._cache[key] = (
            LocalCacheEntry(
                response=response,
                model=model,
                created_at=now,
                expires_at=(
                    now + self.ttl_seconds
                ),
                input_tokens=input_tokens,
                output_tokens=output_tokens,
            )
        )

    def invalidate(
        self,
        prompt: str,
        model: str,
    ) -> bool:

        key = self.build_key(
            prompt,
            model,
        )

        return (
            self._cache.pop(
                key,
                None,
            )
            is not None
        )

    def invalidate_all(
        self,
    ) -> int:

        count = len(
            self._cache
        )

        self._cache.clear()

        return count