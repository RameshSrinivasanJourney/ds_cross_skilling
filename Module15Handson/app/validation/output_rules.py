import re


class OutputRuleValidator:
    """Perform deterministic checks on model output."""

    def __init__(
        self,
        max_characters: int = 10000,
    ) -> None:

        self.max_characters = (
            max_characters
        )

        self.forbidden_patterns = [
            r"\bapi[_ -]?key\b",
            r"\bsecret[_ -]?key\b",
            r"\bpassword\s*=",
            r"\bBEGIN\s+PRIVATE\s+KEY\b",
        ]

    def validate(
        self,
        text: str,
    ) -> list[str]:

        errors: list[str] = []

        if not text.strip():
            errors.append(
                "Output is empty."
            )

            return errors

        if len(text) > self.max_characters:
            errors.append(
                "Output exceeds the maximum "
                "allowed length."
            )

        for pattern in (
            self.forbidden_patterns
        ):

            if re.search(
                pattern,
                text,
                re.IGNORECASE,
            ):

                errors.append(
                    "Output contains a "
                    "forbidden sensitive-data pattern."
                )

        return list(
            dict.fromkeys(
                errors
            )
        )