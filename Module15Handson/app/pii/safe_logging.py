import re


class SafeLogSanitizer:
    """Final safety layer before PII reaches logs."""

    PATTERNS = [
        (
            re.compile(
                r"\b[A-Za-z0-9._%+-]+@"
                r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
            ),
            "[REDACTED_EMAIL]",
        ),
        (
            re.compile(
                r"(?<!\d)"
                r"(?:\+\d{1,3}[\s.-]?)?"
                r"\d{3,5}"
                r"[\s.-]?"
                r"\d{3,5}"
                r"(?!\d)"
            ),
            "[REDACTED_PHONE]",
        ),
    ]

    def sanitize(
        self,
        text: str,
    ) -> str:

        result = text

        for pattern, replacement in (
            self.PATTERNS
        ):

            result = pattern.sub(
                replacement,
                result,
            )

        return result