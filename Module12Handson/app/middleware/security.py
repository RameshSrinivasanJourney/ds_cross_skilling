import time
from collections import defaultdict

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.core.config import (
    RATE_LIMIT,
)


class RateLimitMiddleware(
    BaseHTTPMiddleware
):
    """Simple in-memory request rate limiter."""

    def __init__(
        self,
        app,
    ):
        super().__init__(app)

        self.requests = defaultdict(list)

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        client_ip = (
            request.client.host
            if request.client
            else "unknown"
        )

        now = time.time()

        window_start = (
            now - 60
        )

        timestamps = self.requests[
            client_ip
        ]

        self.requests[
            client_ip
        ] = [
            timestamp
            for timestamp in timestamps
            if timestamp >= window_start
        ]

        if len(
            self.requests[client_ip]
        ) >= RATE_LIMIT:

            return JSONResponse(
                status_code=429,
                content={
                    "detail": (
                        "Rate limit exceeded."
                    )
                },
            )

        self.requests[
            client_ip
        ].append(now)

        return await call_next(
            request
        )