import time


def successful_tool(value: str) -> str:
    """Return a successful result."""

    return f"Processed: {value}"


def failing_tool() -> str:
    """Deliberately raise an exception."""

    raise RuntimeError(
        "Simulated tool failure."
    )


def slow_tool(
    seconds: float = 5.0,
) -> str:
    """Deliberately sleep to test timeout handling."""

    time.sleep(seconds)

    return (
        f"Completed after {seconds} seconds."
    )