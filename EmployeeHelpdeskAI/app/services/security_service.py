from app.security.input_validator import validate_input
from app.security.prompt_injection import is_prompt_injection
from app.security.prompt_leak_guard import is_prompt_leak_attempt
from app.security.jailbreak_guard import is_jailbreak_attempt
from app.security.output_filter import filter_output

from app.security.security_messages import (
    PROMPT_INJECTION_BLOCKED,
    PROMPT_LEAK_BLOCKED,
    JAILBREAK_BLOCKED
)


class SecurityService:

    def validate_request(self, prompt: str):

        is_valid, message = validate_input(prompt)

        if not is_valid:
            return False, message

        if is_prompt_injection(prompt):
            return False, PROMPT_INJECTION_BLOCKED

        if is_prompt_leak_attempt(prompt):
            return False, PROMPT_LEAK_BLOCKED

        if is_jailbreak_attempt(prompt):
            return False, JAILBREAK_BLOCKED

        return True, ""

    def validate_response(self, answer: str):

        return filter_output(answer)