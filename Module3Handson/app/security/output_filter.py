class OutputFilter:

    BLOCKED_PATTERNS = [

        "system prompt",

        "api key",

        "password",

        "secret",

        "token"

    ]

    @staticmethod
    def filter(text: str):

        lower = text.lower()

        for pattern in OutputFilter.BLOCKED_PATTERNS:

            if pattern in lower:

                return (
                    "The generated response contains "
                    "restricted information and cannot "
                    "be displayed."
                )

        return text