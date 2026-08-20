from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_first_agent() -> Agent:
    """Create the first CrewAI agent."""

    return Agent(
        role="Python Tutor",
        goal="Explain Python concepts clearly to beginners.",
        backstory=(
            "You are an experienced Python instructor "
            "who explains technical concepts using simple "
            "examples and practical explanations."
        ),
        llm=ollama_llm,
        verbose=True,
    )