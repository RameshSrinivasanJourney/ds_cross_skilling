from app.agents.llm import ask_llm


def planner_agent(goal: str) -> str:
    """Create a structured plan for the user goal."""

    return ask_llm(
        system_prompt=(
            "You are a Planning Agent.\n"
            "Your responsibility is to break a complex "
            "goal into clear, actionable subtasks.\n"
            "Do not perform the tasks yourself.\n"
            "Return a numbered plan."
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            "Create a concise execution plan."
        ),
    )