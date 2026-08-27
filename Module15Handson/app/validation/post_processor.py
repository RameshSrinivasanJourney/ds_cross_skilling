import re


class OutputPostProcessor:
    """Apply deterministic output cleanup."""

    def process(
        self,
        text: str,
    ) -> str:

        # Remove common markdown fence wrappers.
        text = re.sub(
            r"^```(?:text|json)?\s*",
            "",
            text.strip(),
            flags=re.IGNORECASE,
        )

        text = re.sub(
            r"\s*```$",
            "",
            text.strip(),
        )

        # Collapse excessive whitespace.
        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        # Avoid excessive blank lines.
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()