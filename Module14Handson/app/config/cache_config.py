import os


CACHE_TTL_SECONDS = int(
    os.getenv(
        "MODULE14_CACHE_TTL",
        "300",
    )
)

REDIS_URL = os.getenv(
    "MODULE14_REDIS_URL",
    "redis://localhost:6379/0",
)

CACHE_NAMESPACE = os.getenv(
    "MODULE14_CACHE_NAMESPACE",
    "module14",
)