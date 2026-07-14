import re

PROMPT_LEAK_PATTERNS = [

    r"system prompt",
    r"hidden prompt",
    r"developer message",
    r"developer prompt",
    r"internal prompt",
    r"show your instructions",
    r"reveal your instructions",
    r"print your instructions",
    r"repeat your instructions",
    r"repeat everything above",
    r"show hidden instructions",
    r"what were your initial instructions",
    r"display your prompt",
]


def is_prompt_leak_attempt(text: str) -> bool:

    text = text.lower()

    for pattern in PROMPT_LEAK_PATTERNS:

        if re.search(pattern, text):
            return True

    return False