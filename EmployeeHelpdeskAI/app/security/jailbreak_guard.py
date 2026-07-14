import re

JAILBREAK_PATTERNS = [

    r"ignore all safety",

    r"ignore all restrictions",

    r"ignore all rules",

    r"do anything now",

    r"\bdan\b",

    r"unrestricted ai",

    r"no restrictions",

    r"bypass safety",

    r"disable safety",

    r"pretend you have no limitations",

    r"developer mode",

    r"god mode",

    r"ignore your guidelines",

    r"follow my rules instead",

    r"override your instructions",

]


def is_jailbreak_attempt(text: str) -> bool:

    text = text.lower()

    for pattern in JAILBREAK_PATTERNS:

        if re.search(pattern, text):
            return True

    return False