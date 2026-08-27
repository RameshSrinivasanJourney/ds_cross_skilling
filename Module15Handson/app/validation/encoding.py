import unicodedata


class CharacterSanitizer:
    """Normalize Unicode and remove control characters."""

    def sanitize(
        self,
        text: str,
    ) -> str:

        normalized = unicodedata.normalize(
            "NFKC",
            text,
        )

        cleaned = "".join(
            character
            for character in normalized
            if (
                character in "\n\t\r"
                or not unicodedata.category(
                    character
                ).startswith("C")
            )
        )

        return cleaned.strip()