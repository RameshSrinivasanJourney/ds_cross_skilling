from app.security.base_guard import BaseGuard
class PromptInjectionGuard(BaseGuard):

    BLOCKED_PATTERNS = [

        "ignore previous instructions",

        "ignore all previous instructions",

        "forget your instructions",

        "reveal system prompt",

        "show your prompt",

        "act as",

        "you are now",

        "pretend to be",

        "developer mode"

    ]