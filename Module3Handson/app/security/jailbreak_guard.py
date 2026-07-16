from app.security.base_guard import BaseGuard
class JailbreakGuard(BaseGuard):

    BLOCKED_PATTERNS = [

        "developer mode",

        "pretend",

        "roleplay",

        "act as",

        "unrestricted ai",

        "ignore all policies",

        "disable safety",

        "bypass",

        "jailbreak",

        "you have no restrictions",

        "for educational purposes"

    ]