from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_research_agent() -> Agent:
    return Agent(
        role="Research Specialist",
        goal=(
            "Research technical topics accurately and "
            "identify the most important facts."
        ),
        backstory=(
            "You are a careful technical researcher who "
            "focuses on accuracy, useful details, and "
            "clear evidence."
        ),
        llm=ollama_llm,
        verbose=True,
    )