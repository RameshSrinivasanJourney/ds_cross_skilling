import re


BLOCKED_PATTERNS = [

    r"system prompt",

    r"developer instructions",

    r"developer message",

    r"internal prompt",

    r"hidden prompt",

    r"api key",

    r"secret key",

    r"password",

    r"token",

    r"bearer",

]


def filter_output(text: str):

    if text is None:
        return False, "No response generated."

    lower = text.lower()

    for pattern in BLOCKED_PATTERNS:

        if re.search(pattern, lower):

            return (
                False,
                "The AI response was blocked because it "
                "contained restricted information."
            )

    return True, text