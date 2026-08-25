import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

PHONE_PATTERN = re.compile(
    r"""
    (?<!\d)
    (?:
        \+\d{1,3}[\s.-]?
    )?
    (?:
        \(\d{2,4}\)[\s.-]?
    )?
    \d{3,5}
    [\s.-]?
    \d{3,5}
    (?!\d)
    """,
    re.VERBOSE,
)

CREDIT_CARD_PATTERN = re.compile(
    r"\b(?:\d[ -]*?){13,19}\b"
)


def scrub_pii(
    value: str,
) -> str:
    """Redact common PII patterns."""

    if not value:
        return value

    value = EMAIL_PATTERN.sub(
        "[REDACTED_EMAIL]",
        value,
    )

    value = PHONE_PATTERN.sub(
        "[REDACTED_PHONE]",
        value,
    )

    value = CREDIT_CARD_PATTERN.sub(
        "[REDACTED_CARD]",
        value,
    )

    return value