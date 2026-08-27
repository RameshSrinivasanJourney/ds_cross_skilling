from enum import Enum


class RiskLevel(str, Enum):
    SAFE = "safe"
    REVIEW = "review"
    BLOCK = "block"


class RiskCategory(str, Enum):
    HARMFUL = "harmful"
    VIOLENCE = "violence"
    SELF_HARM = "self_harm"
    HATE = "hate"
    SEXUAL = "sexual"
    ILLEGAL = "illegal"
    PRIVACY = "privacy"
    BIAS = "bias"
    COMPLIANCE = "compliance"
    PROMPT_INJECTION = "prompt_injection"