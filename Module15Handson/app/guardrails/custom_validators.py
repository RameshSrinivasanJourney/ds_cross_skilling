import re


class NoPIIValidator:
    """Simple custom validator for common PII."""

    def validate(
        self,
        value: str,
    ) -> str:

        email_pattern = (
            r"\b[A-Za-z0-9._%+-]+@"
            r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        )

        phone_pattern = (
            r"(?<!\d)"
            r"(?:\+\d{1,3}[\s.-]?)?"
            r"\d{3,5}"
            r"[\s.-]?"
            r"\d{3,5}"
            r"(?!\d)"
        )

        if re.search(
            email_pattern,
            value,
        ):

            raise ValueError(
                "Output contains an email address."
            )

        if re.search(
            phone_pattern,
            value,
        ):

            raise ValueError(
                "Output contains a phone number."
            )

        return value


class NoURLValidator:
    """Simple custom URL validator."""

    def validate(
        self,
        value: str,
    ) -> str:

        url_pattern = (
            r"https?://\S+"
        )

        if re.search(
            url_pattern,
            value,
            re.IGNORECASE,
        ):

            raise ValueError(
                "Output contains a URL."
            )

        return value


class NoToxicTermsValidator:
    """
    Small educational toxicity validator.

    This is not a production toxicity classifier.
    """

    BLOCKED_TERMS = {
        "explicit_slur",
        "violent_threat",
    }

    def validate(
        self,
        value: str,
    ) -> str:

        lowered = value.lower()

        for term in self.BLOCKED_TERMS:

            if term in lowered:

                raise ValueError(
                    "Output contains a "
                    "configured toxic term."
                )

        return value