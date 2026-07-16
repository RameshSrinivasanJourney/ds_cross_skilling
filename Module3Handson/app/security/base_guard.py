class BaseGuard:

    BLOCKED_PATTERNS = []

    @classmethod
    def is_safe(cls, user_input: str):

        text = user_input.lower()

        return not any(

            pattern in text

            for pattern in cls.BLOCKED_PATTERNS

        )