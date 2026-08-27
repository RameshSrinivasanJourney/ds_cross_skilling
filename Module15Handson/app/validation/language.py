from langdetect import (
    DetectorFactory,
    LangDetectException,
    detect,
)


# Make langdetect deterministic.
DetectorFactory.seed = 0


class LanguageValidator:
    """Validate input language."""

    def __init__(
        self,
        allowed_languages: set[str] | None = None,
    ) -> None:

        self.allowed_languages = (
            allowed_languages
            or {"en"}
        )

    def detect(
        self,
        text: str,
    ) -> str | None:

        if not text.strip():
            return None

        try:
            return detect(text)

        except LangDetectException:
            return None

    def validate(
        self,
        text: str,
    ) -> str | None:

        language = self.detect(
            text
        )

        if language is None:
            return (
                "Unable to determine "
                "input language."
            )

        if (
            language
            not in self.allowed_languages
        ):
            return (
                f"Unsupported input "
                f"language: {language}"
            )

        return None