from enum import Enum


class ModerationDecision(str, Enum):
    ALLOW = "allow"
    REVIEW = "review"
    BLOCK = "block"


class ModerationCategory(str, Enum):
    VIOLENCE = "violence"
    SELF_HARM = "self_harm"
    HATE = "hate"
    SEXUAL = "sexual"
    ILLEGAL = "illegal"
    PRIVACY = "privacy"
    PROMPT_INJECTION = "prompt_injection"
    UNSUPPORTED = "unsupported"