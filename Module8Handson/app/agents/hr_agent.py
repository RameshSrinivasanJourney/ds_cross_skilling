from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_hr_agent() -> Agent:
    return Agent(
        role="HR Policy Specialist",
        goal=(
            "Analyze employee HR questions and provide "
            "accurate policy-oriented guidance."
        ),
        backstory=(
            "You are an experienced HR policy specialist "
            "who understands employee policies and "
            "organizational procedures."
        ),
        llm=ollama_llm,
        verbose=True,
        allow_delegation=False,
    )