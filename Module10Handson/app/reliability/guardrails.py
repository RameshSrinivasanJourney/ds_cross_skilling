def validate_agent_output(
    output: str,
    *,
    min_length: int = 10,
    max_length: int = 5000,
) -> str:
    """Validate an agent's output."""

    if not output or not output.strip():
        raise ValueError(
            "Agent output is empty."
        )

    cleaned = output.strip()

    if len(cleaned) < min_length:
        raise ValueError(
            "Agent output is too short."
        )

    if len(cleaned) > max_length:
        raise ValueError(
            "Agent output exceeds the maximum "
            "allowed length."
        )

    return cleaned