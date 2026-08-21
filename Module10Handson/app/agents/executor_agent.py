from app.agents.llm import ask_llm


def executor_agent(
    goal: str,
    plan: str,
    research: str,
) -> str:
    """Execute the planned work using the available information."""

    return ask_llm(
        system_prompt=(
            "You are an Execution Agent.\n"
            "Your responsibility is to turn the plan and "
            "research into concrete results.\n"
            "Do not invent information that is not supported "
            "by the research."
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            f"Plan:\n{plan}\n\n"
            f"Research:\n{research}\n\n"
            "Execute the required work and provide the "
            "result for the writer."
        ),
    )