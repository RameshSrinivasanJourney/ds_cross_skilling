from app.validation.encoding import (
    CharacterSanitizer,
)

from app.validation.language import (
    LanguageValidator,
)

from app.validation.length_validator import (
    InputLengthValidator,
)

from app.validation.prompt_injection import (
    PromptInjectionDetector,
)

from app.validation.topic_filter import (
    TopicFilter,
)

from app.validation.validation_result import (
    ValidationResult,
)


class InputValidator:
    """Run all input validation checks."""

    def __init__(
        self,
        max_characters: int = 4000,
        allowed_languages: set[str] | None = None,
    ) -> None:

        self.sanitizer = (
            CharacterSanitizer()
        )

        self.injection_detector = (
            PromptInjectionDetector()
        )

        self.topic_filter = (
            TopicFilter()
        )

        self.length_validator = (
            InputLengthValidator(
                max_characters
            )
        )

        self.language_validator = (
            LanguageValidator(
                allowed_languages
            )
        )

    def validate(
        self,
        text: str,
    ) -> ValidationResult:

        reasons = []
        categories = []

        if text is None:

            return ValidationResult(
                valid=False,
                normalized_text="",
                reasons=[
                    "Input cannot be null."
                ],
                categories=[
                    "null_input"
                ],
            )

        # 1. Sanitize
        normalized = (
            self.sanitizer.sanitize(
                text
            )
        )

        if not normalized:

            return ValidationResult(
                valid=False,
                normalized_text="",
                reasons=[
                    "Input is empty."
                ],
                categories=[
                    "empty_input"
                ],
            )

        # 2. Length
        length_error = (
            self.length_validator.validate(
                normalized
            )
        )

        if length_error:

            return ValidationResult(
                valid=False,
                normalized_text=normalized,
                reasons=[
                    length_error
                ],
                categories=[
                    "length"
                ],
            )

        # 3. Prompt injection
        injection_matches = (
            self.injection_detector.detect(
                normalized
            )
        )

        if injection_matches:

            reasons.append(
                "Potential prompt injection "
                "detected."
            )

            categories.append(
                "prompt_injection"
            )

        # 4. Disallowed topics
        blocked_topics = (
            self.topic_filter.detect(
                normalized
            )
        )

        if blocked_topics:

            categories.extend(
                blocked_topics
            )

            reasons.append(
                "Disallowed topic detected."
            )

        # 5. Language
        language_error = (
            self.language_validator.validate(
                normalized
            )
        )

        if language_error:

            reasons.append(
                language_error
            )

            categories.append(
                "language"
            )

        categories = list(
            dict.fromkeys(
                categories
            )
        )

        reasons = list(
            dict.fromkeys(
                reasons
            )
        )

        return ValidationResult(
            valid=not categories,
            normalized_text=normalized,
            reasons=reasons,
            categories=categories,
        )