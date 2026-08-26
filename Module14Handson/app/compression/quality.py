def keyword_quality(
    answer: str,
    required_terms: list[str],
) -> float:
    """Simple educational quality score."""

    if not required_terms:
        return 1.0

    answer_lower = answer.lower()

    matched = sum(
        1
        for term in required_terms
        if term.lower()
        in answer_lower
    )

    return matched / len(
        required_terms
    )