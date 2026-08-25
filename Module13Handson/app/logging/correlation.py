import uuid


def create_correlation_id() -> str:
    """Create a unique request correlation ID."""

    return str(
        uuid.uuid4()
    )