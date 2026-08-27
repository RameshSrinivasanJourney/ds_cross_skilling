import re


class PIITokenMapper:
    """Create reversible application-level PII tokens."""

    EMAIL_PATTERN = re.compile(
        r"\b[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    PHONE_PATTERN = re.compile(
        r"(?<!\d)"
        r"(?:\+\d{1,3}[\s.-]?)?"
        r"\d{3,5}"
        r"[\s.-]?"
        r"\d{3,5}"
        r"(?!\d)"
    )

    def __init__(self) -> None:

        self.mapping: dict[
            str,
            str,
        ] = {}

        self.counters = {
            "EMAIL": 0,
            "PHONE": 0,
        }

    def replace(
        self,
        text: str,
    ) -> str:

        def email_replacer(match):

            self.counters["EMAIL"] += 1

            token = (
                f"<EMAIL_"
                f"{self.counters['EMAIL']}>"
            )

            self.mapping[token] = (
                match.group(0)
            )

            return token

        def phone_replacer(match):

            self.counters["PHONE"] += 1

            token = (
                f"<PHONE_"
                f"{self.counters['PHONE']}>"
            )

            self.mapping[token] = (
                match.group(0)
            )

            return token

        text = self.EMAIL_PATTERN.sub(
            email_replacer,
            text,
        )

        text = self.PHONE_PATTERN.sub(
            phone_replacer,
            text,
        )

        return text

    def restore(
        self,
        text: str,
    ) -> str:

        for token, original in (
            self.mapping.items()
        ):

            text = text.replace(
                token,
                original,
            )

        return text