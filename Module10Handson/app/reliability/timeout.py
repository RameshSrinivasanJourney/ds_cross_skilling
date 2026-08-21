from concurrent.futures import (
    ThreadPoolExecutor,
    TimeoutError,
)
from collections.abc import Callable
from typing import Any


def execute_with_timeout(
    function: Callable[..., Any],
    *args: Any,
    timeout_seconds: float = 3.0,
    **kwargs: Any,
) -> Any:
    """Execute a function with a timeout."""

    with ThreadPoolExecutor(
        max_workers=1
    ) as executor:

        future = executor.submit(
            function,
            *args,
            **kwargs,
        )

        try:
            return future.result(
                timeout=timeout_seconds
            )

        except TimeoutError as exc:
            raise TimeoutError(
                f"Operation timed out after "
                f"{timeout_seconds} seconds."
            ) from exc