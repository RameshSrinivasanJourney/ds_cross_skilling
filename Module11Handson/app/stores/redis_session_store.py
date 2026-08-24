import json
from typing import Any

from redis import Redis

from app.stores.state_store import StateStore


class RedisSessionStore(StateStore):
    """Redis-backed session state store."""

    def __init__(
        self,
        url: str = "redis://localhost:6379/0",
    ) -> None:

        self.redis = Redis.from_url(
            url,
            decode_responses=True,
        )

    def save(
        self,
        key: str,
        value: dict[str, Any],
    ) -> None:

        self.redis.set(
            key,
            json.dumps(value),
        )

    def get(
        self,
        key: str,
    ) -> dict[str, Any] | None:

        value = self.redis.get(key)

        if value is None:
            return None

        return json.loads(value)

    def ping(self) -> bool:
        return bool(
            self.redis.ping()
        )