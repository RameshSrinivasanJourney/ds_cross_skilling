from app.agents.llm import ask_llm


def researcher_agent(
    goal: str,
    plan: str = "",
) -> str:
    """Research the information needed for the task."""

    return ask_llm(
        system_prompt=(
            "You are a Research Agent.\n"
            "Your responsibility is to identify useful "
            "facts and information for the assigned goal.\n"
            "Do not invent company-specific facts.\n"
            "Clearly identify uncertainty."
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            f"Plan:\n{plan}\n\n"
            "Produce useful research findings."
        ),
    )