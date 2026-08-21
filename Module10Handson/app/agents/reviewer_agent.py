from app.agents.llm import ask_llm


def reviewer_agent(
    question: str,
    draft: str,
) -> str:
    """Review the generated answer."""

    return ask_llm(
        system_prompt=(
            "You are a strict Review Agent. "
            "Check whether the draft directly answers "
            "the question, contains unsupported claims, "
            "or has logical errors."
        ),
        user_prompt=(
            f"Question:\n"
            f"{question}\n\n"
            f"Draft Answer:\n"
            f"{draft}\n\n"
            "Return either:\n"
            "PASS\n"
            "or\n"
            "REVISE: <specific issue>"
        ),
    )