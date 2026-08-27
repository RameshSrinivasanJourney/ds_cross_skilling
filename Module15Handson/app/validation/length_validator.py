class InputLengthValidator:

    def __init__(
        self,
        max_characters: int = 4000,
    ) -> None:

        self.max_characters = (
            max_characters
        )

    def validate(
        self,
        text: str,
    ) -> str | None:

        if len(text) > self.max_characters:

            return (
                f"Input exceeds the "
                f"{self.max_characters} "
                f"character limit."
            )

        return None