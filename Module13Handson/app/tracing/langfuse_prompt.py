from app.tracing.langfuse_client import langfuse


PROMPT_NAME = "module13-answer-prompt"


def get_answer_prompt(
    question: str,
) -> str:
    """Retrieve and compile the managed Langfuse prompt."""

    prompt = langfuse.get_prompt(
        PROMPT_NAME
    )

    return prompt.compile(
        question=question
    )