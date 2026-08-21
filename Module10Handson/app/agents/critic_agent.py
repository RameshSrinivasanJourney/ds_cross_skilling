from app.agents.llm import ask_llm


def critic_agent(
    goal: str,
    draft: str,
) -> str:
    """Review the draft and identify issues."""

    return ask_llm(
        system_prompt=(
            "You are a strict Critic and Review Agent.\n"
            "Check the draft for correctness, completeness, "
            "unsupported claims, and whether it answers "
            "the user's goal.\n\n"
            "Return exactly one of:\n"
            "PASS\n"
            "or\n"
            "REVISE: <specific problems>"
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            f"Draft:\n{draft}"
        ),
    )