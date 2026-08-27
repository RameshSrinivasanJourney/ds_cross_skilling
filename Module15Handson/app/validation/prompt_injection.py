import re


class PromptInjectionDetector:
    """Detect common prompt-injection patterns."""

    PATTERNS = [
        r"\bignore\s+(?:all\s+)?previous\s+instructions\b",
        r"\bignore\s+(?:all\s+)?prior\s+instructions\b",
        r"\breveal\s+your\s+system\s+prompt\b",
        r"\bshow\s+your\s+system\s+prompt\b",
        r"\breveal\s+the\s+developer\s+message\b",
        r"\bshow\s+the\s+developer\s+message\b",
        r"\bforget\s+(?:all\s+)?previous\s+instructions\b",
        r"\bdisregard\s+(?:all\s+)?previous\s+instructions\b",
        r"\bprint\s+the\s+system\s+prompt\b",
    ]

    def detect(
        self,
        text: str,
    ) -> list[str]:

        normalized = re.sub(
            r"\s+",
            " ",
            text.lower().strip(),
        )

        matches = []

        for pattern in self.PATTERNS:

            if re.search(
                pattern,
                normalized,
            ):

                matches.append(
                    pattern
                )

        return list(
            dict.fromkeys(
                matches
            )
        )