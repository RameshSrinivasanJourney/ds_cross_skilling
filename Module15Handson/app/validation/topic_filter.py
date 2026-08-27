import re


class TopicFilter:
    """Block clearly disallowed request categories."""

    BLOCKED_PATTERNS = {
        "violent_harm": [
            r"\bhow\s+to\s+build\s+a\s+bomb\b",
            r"\bhow\s+can\s+i\s+build\s+a\s+bomb\b",
            r"\bhow\s+to\s+make\s+a\s+weapon\b",
            r"\bhow\s+can\s+i\s+make\s+a\s+weapon\b",
            r"\bhow\s+to\s+kill\s+someone\b",
        ],
        "credential_theft": [
            r"\bsteal\s+someone'?s\s+password\b",
            r"\bhow\s+to\s+steal\s+credentials\b",
        ],
    }

    def detect(
        self,
        text: str,
    ) -> list[str]:

        normalized = re.sub(
            r"\s+",
            " ",
            text.lower().strip(),
        )

        categories = []

        for category, patterns in (
            self.BLOCKED_PATTERNS.items()
        ):

            if any(
                re.search(
                    pattern,
                    normalized,
                )
                for pattern in patterns
            ):

                categories.append(
                    category
                )

        return categories