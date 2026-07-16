class InputValidator:

    MAX_INPUT_LENGTH = 1000

    BLOCKED_PATTERNS = [

        "<script",

        "</script>",

        "drop table",

        "delete from",

        "truncate table"

    ]

    @staticmethod
    def validate(user_input: str):

        if not user_input:

            return False, "Input cannot be empty."

        if not user_input.strip():

            return False, "Input cannot be empty."

        if len(user_input) > InputValidator.MAX_INPUT_LENGTH:

            return False, (
                f"Input exceeds "
                f"{InputValidator.MAX_INPUT_LENGTH} characters."
            )

        text = user_input.lower()

        for pattern in InputValidator.BLOCKED_PATTERNS:

            if pattern in text:

                return False, (
                    "Input contains blocked content."
                )

        return True, None