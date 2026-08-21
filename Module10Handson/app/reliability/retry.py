from collections.abc import Callable
from typing import Any


def execute_with_retry(
    function: Callable[..., Any],
    *args: Any,
    max_retries: int = 2,
    **kwargs: Any,
) -> Any:
    """Execute a function with bounded retries."""

    last_error: Exception | None = None

    for attempt in range(
        1,
        max_retries + 2,
    ):
        try:
            return function(
                *args,
                **kwargs,
            )

        except Exception as exc:
            last_error = exc

            print(
                f"Attempt {attempt} failed: "
                f"{exc}"
            )

    raise RuntimeError(
        f"Operation failed after "
        f"{max_retries + 1} attempts."
    ) from last_error