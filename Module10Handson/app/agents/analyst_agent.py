from app.agents.llm import ask_llm


def analyst_agent(
    question: str,
    research: str,
) -> str:
    """Analyze the research."""

    return ask_llm(
        system_prompt=(
            "You are an Analysis Agent. "
            "Analyze the supplied research and "
            "identify the most relevant conclusions. "
            "Point out uncertainty when information "
            "is insufficient."
        ),
        user_prompt=(
            f"Employee Question:\n"
            f"{question}\n\n"
            f"Research:\n"
            f"{research}"
        ),
    )