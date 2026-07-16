from app.security.base_guard import BaseGuard
class PromptLeakGuard(BaseGuard):

    BLOCKED_PATTERNS = [

        "system prompt",

        "hidden prompt",

        "previous instructions",

        "your instructions",

        "internal prompt",

        "show prompt",

        "reveal prompt",

        "repeat instructions",

        "what were you told",

        "developer instructions"

    ]
