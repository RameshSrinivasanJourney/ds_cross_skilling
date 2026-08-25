import json
import time
import uuid
from datetime import datetime, timezone

from redis import Redis


SESSION_TTL_SECONDS = 1800


class SessionStore:
    """Redis-backed session store."""

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
    ) -> None:

        self.redis = Redis.from_url(
            redis_url,
            decode_responses=True,
        )

    def _build_key(
        self,
        tenant_id: str,
        conversation_id: str,
    ) -> str:

        return (
            f"session:"
            f"{tenant_id}:"
            f"{conversation_id}"
        )

    def create_session(
        self,
        tenant_id: str,
    ) -> dict:

        conversation_id = str(
            uuid.uuid4()
        )

        now = datetime.now(
            timezone.utc
        ).isoformat()

        session = {
            "tenant_id": tenant_id,
            "conversation_id": conversation_id,
            "messages": [],
            "created_at": now,
            "last_accessed_at": now,
        }

        key = self._build_key(
            tenant_id,
            conversation_id,
        )

        self.redis.setex(
            key,
            SESSION_TTL_SECONDS,
            json.dumps(session),
        )

        return session

    def get_session(
        self,
        tenant_id: str,
        conversation_id: str,
    ) -> dict | None:

        key = self._build_key(
            tenant_id,
            conversation_id,
        )

        raw = self.redis.get(key)

        if raw is None:
            return None

        session = json.loads(raw)

        session["last_accessed_at"] = (
            datetime.now(
                timezone.utc
            ).isoformat()
        )

        self.redis.setex(
            key,
            SESSION_TTL_SECONDS,
            json.dumps(session),
        )

        return session

    def update_session(
        self,
        tenant_id: str,
        conversation_id: str,
        session: dict,
    ) -> None:

        key = self._build_key(
            tenant_id,
            conversation_id,
        )

        session["last_accessed_at"] = (
            datetime.now(
                timezone.utc
            ).isoformat()
        )

        self.redis.setex(
            key,
            SESSION_TTL_SECONDS,
            json.dumps(session),
        )

    def delete_session(
        self,
        tenant_id: str,
        conversation_id: str,
    ) -> bool:

        key = self._build_key(
            tenant_id,
            conversation_id,
        )

        return bool(
            self.redis.delete(key)
        )

    def ttl(
        self,
        tenant_id: str,
        conversation_id: str,
    ) -> int:

        key = self._build_key(
            tenant_id,
            conversation_id,
        )

        return self.redis.ttl(key)