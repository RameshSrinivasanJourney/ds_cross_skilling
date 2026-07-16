from app.security.input_validator import InputValidator
from app.security.prompt_injection import PromptInjectionGuard
from app.security.prompt_leak_guard import PromptLeakGuard
from app.security.jailbreak_guard import JailbreakGuard


class SecurityService:

    @staticmethod
    def validate(user_input: str):

        valid, error = InputValidator.validate(user_input)

        if not valid:
            return False, error

        if not PromptInjectionGuard.is_safe(user_input):
            return (
                False,
                "Potential prompt injection detected. Request rejected."
            )

        if not PromptLeakGuard.is_safe(user_input):
            return (
                False,
                "Sorry, I cannot disclose internal system instructions."
            )

        if not JailbreakGuard.is_safe(user_input):
            return (
                False,
                "Potential jailbreak attempt detected. Request rejected."
            )

        return True, None