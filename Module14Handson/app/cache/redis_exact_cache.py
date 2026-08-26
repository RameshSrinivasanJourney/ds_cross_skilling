import hashlib
import json
import time
from dataclasses import asdict, dataclass

from redis import Redis

from app.config.cache_config import (
    CACHE_NAMESPACE,
    CACHE_TTL_SECONDS,
    REDIS_URL,
)


@dataclass
class CachedResponse:
    response: str
    model: str
    created_at: float
    input_tokens: int
    output_tokens: int


class RedisExactCache:
    """Redis exact-match cache with TTL."""

    def __init__(
        self,
        redis_url: str = REDIS_URL,
        ttl_seconds: int = CACHE_TTL_SECONDS,
    ) -> None:

        self.ttl_seconds = ttl_seconds

        self.redis = Redis.from_url(
            redis_url,
            decode_responses=True,
        )

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

        normalized = (
            self.normalize_prompt(
                prompt
            )
        )

        material = (
            f"{model}:{normalized}"
        )

        prompt_hash = hashlib.sha256(
            material.encode("utf-8")
        ).hexdigest()

        return (
            f"{CACHE_NAMESPACE}:"
            f"exact:{prompt_hash}"
        )

    def get(
        self,
        prompt: str,
        model: str,
    ) -> CachedResponse | None:

        key = self.build_key(
            prompt,
            model,
        )

        raw = self.redis.get(
            key
        )

        if raw is None:
            return None

        data = json.loads(
            raw
        )

        return CachedResponse(
            **data
        )

    def set(
        self,
        prompt: str,
        model: str,
        response: str,
        input_tokens: int,
        output_tokens: int,
    ) -> None:

        key = self.build_key(
            prompt,
            model,
        )

        value = CachedResponse(
            response=response,
            model=model,
            created_at=time.time(),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

        self.redis.setex(
            key,
            self.ttl_seconds,
            json.dumps(
                asdict(value)
            ),
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

        return bool(
            self.redis.delete(key)
        )

    def invalidate_all(
        self,
    ) -> int:

        pattern = (
            f"{CACHE_NAMESPACE}:exact:*"
        )

        keys = list(
            self.redis.scan_iter(
                match=pattern
            )
        )

        if not keys:
            return 0

        return int(
            self.redis.delete(
                *keys
            )
        )

    def ttl(
        self,
        prompt: str,
        model: str,
    ) -> int:

        key = self.build_key(
            prompt,
            model,
        )

        return self.redis.ttl(
            key
        )