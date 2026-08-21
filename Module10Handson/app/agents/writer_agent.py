from app.agents.llm import ask_llm


def writer_agent(
    goal: str,
    research: str,
    execution_result: str,
) -> str:
    """Generate the final user-facing response."""

    return ask_llm(
        system_prompt=(
            "You are a professional Writer Agent.\n"
            "Create a clear, concise response for the user.\n"
            "Use only supported information from the "
            "research and execution results.\n"
            "Do not invent facts."
        ),
        user_prompt=(
            f"Goal:\n{goal}\n\n"
            f"Research:\n{research}\n\n"
            f"Execution Result:\n{execution_result}\n\n"
            "Write the final response."
        ),
    )