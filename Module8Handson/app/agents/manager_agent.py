from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_manager_agent() -> Agent:
    return Agent(
        role="Employee Assistant Manager",
        goal=(
            "Coordinate specialist agents and produce "
            "the best possible response to an employee request."
        ),
        backstory=(
            "You are an experienced team manager who "
            "delegates work to specialists and combines "
            "their results into a useful final answer."
        ),
        llm=ollama_llm,
        verbose=True,
        allow_delegation=True,
    )