PROMPT_INJECTION_BLOCKED = (
    "Your request cannot be processed because it contains "
    "instructions that violate the assistant's security policy."
)

PROMPT_LEAK_BLOCKED = (
    "I can't reveal internal instructions, system prompts, or "
    "implementation details. Please ask an HR-related question."
)

JAILBREAK_BLOCKED = (
    "Your request appears to attempt to bypass the assistant's "
    "security or safety policies and cannot be processed."
)

INPUT_VALIDATION_FAILED = (
    "The request could not be processed because the input is invalid."
)

OUTPUT_FILTER_BLOCKED = (
    "The AI response was blocked because it contained "
    "restricted information."
)