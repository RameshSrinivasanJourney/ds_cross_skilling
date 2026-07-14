import re


SUSPICIOUS_PATTERNS = [

    r"ignore previous instructions",

    r"ignore all instructions",

    r"forget previous instructions",

    r"reveal your system prompt",

    r"show your system prompt",

    r"print your system prompt",

    r"developer message",

    r"act as",

    r"you are now",

    r"pretend to be",

    r"jailbreak",

    r"do anything now",

    r"dan",

    r"system prompt",

    r"hidden prompt",

]


def is_prompt_injection(text: str) -> bool:

    text = text.lower()

    for pattern in SUSPICIOUS_PATTERNS:

        if re.search(pattern, text):
            return True

    return False