from app.agents.llm import ask_llm


def supervisor_agent(
    goal: str,
    plan: str,
    research: str,
    execution_result: str,
    draft: str,
    review: str,
) -> str:
    """Coordinate the specialist outputs."""

    return ask_llm(
        system_prompt=(
            "You are the Supervisor Agent.\n"
            "Your responsibility is to review the work "
            "performed by the specialist agents and decide "
            "whether the final result is ready.\n"
            "If the critic says PASS, return a concise "
            "final response.\n"
            "If the critic says REVISE, explain what "
            "needs to be corrected."
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            f"Plan:\n{plan}\n\n"
            f"Research:\n{research}\n\n"
            f"Execution:\n{execution_result}\n\n"
            f"Draft:\n{draft}\n\n"
            f"Critic Review:\n{review}"
        ),
    )