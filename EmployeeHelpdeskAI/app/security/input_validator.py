import re


MAX_PROMPT_LENGTH = 1000


def validate_input(text: str):

    if text is None:
        return False, "Input cannot be null."

    text = text.strip()

    if len(text) == 0:
        return False, "Please enter a question."

    if len(text) > MAX_PROMPT_LENGTH:
        return False, (
            f"Input exceeds the maximum allowed length "
            f"of {MAX_PROMPT_LENGTH} characters."
        )

    # Too many repeated characters
    if re.search(r"(.)\1{20,}", text):
        return False, (
            "Input contains excessive repeated characters."
        )

    # Very basic HTML detection
    if re.search(r"<[^>]+>", text):
        return False, (
            "HTML content is not allowed."
        )

    # Very basic SQL injection detection
    sql_patterns = [

        r"drop\s+table",

        r"delete\s+from",

        r"truncate\s+table",

        r"union\s+select",

        r"insert\s+into",

        r"update\s+\w+\s+set"

    ]

    lower_text = text.lower()

    for pattern in sql_patterns:

        if re.search(pattern, lower_text):
            return False, (
                "Input contains unsupported content."
            )

    return True, ""