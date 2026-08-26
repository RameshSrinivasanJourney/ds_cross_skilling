from redis import Redis
from redis.exceptions import (
    RedisError,
)

from app.cache.local_exact_cache import (
    LocalExactCache,
)
from app.cache.redis_exact_cache import (
    RedisExactCache,
)
from app.config.cache_config import (
    CACHE_TTL_SECONDS,
    REDIS_URL,
)


def create_exact_cache():
    """Use Redis when available; otherwise use local cache."""

    try:

        redis = Redis.from_url(
            REDIS_URL,
            decode_responses=True,
            socket_connect_timeout=1,
        )

        redis.ping()

        print(
            "Cache backend: Redis"
        )

        return RedisExactCache(
            ttl_seconds=CACHE_TTL_SECONDS
        )

    except RedisError:

        print(
            "Cache backend: Local fallback"
        )

        return LocalExactCache(
            ttl_seconds=CACHE_TTL_SECONDS
        )